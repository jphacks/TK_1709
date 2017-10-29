//
//  DjangoAPI.swift
//  Kashikari
//
//  Created by 山田涼太 on 2017/10/24.
//  Copyright © 2017年 吉野克基. All rights reserved.
//

import Foundation

import Moya
import Alamofire
import SwiftyJSON

enum DjangoAPI {
    case getItems
    case postItem(name: String, description: String, imageUrl: String, price: Int, deadline: String, status: String, username: String)
    case sendImage(img: String)
}


//enum DjangoAPI {
//
//    // images
////    case postImage(image: Image)
//
//    // items
//    case getItems
//    case getItem(itemId: Int)
//    case createItem(name: String, description: String, image_url: String, price: Int, deadline: String, status: String, username: String?)
//
//}


extension DjangoAPI: TargetType {
    
    var baseURL: URL {
        let baseURLString: String = "http://54.64.12.240:8000"
        return URL(string: baseURLString)!
    }
    
    var path: String {
        switch self {
            
        case .getItems,
             .postItem:
            return "/exhibit/items"
        case .sendImage:
            return "/split/"
        }
    }
    
    public var method: Moya.Method {
        switch self {
            
        case .postItem,
             .sendImage:
            return .post
        default:
            return .get
        }
    }
    
    public var parameters: [String: Any]? {
        switch self {
        case .sendImage(let img):
            return ["img": img]
        default:
            return nil

        }
    }
    
    var sampleData: Data {
        return Data()
    }

    var task: Task {
        return .requestPlain
    }
    
    var headers: [String : String]? {
        return nil
    }

}


//extension DjangoAPI: TargetType {
//    var baseURL: URL {
//        let baseURLString: String = "http://54.64.12.240"
//        return URL(string: baseURLString)!
//    }
//
//    var path: String {
//        switch self {
//
////        case .postImage:
////            return "/exhibit/items"
//
//        case .getItems:
//            return "/exhibit/items"
//
//        case .getItem(let itemId):
//            return "/exhibit/items/\(itemId)"
//
//        case .createItem:
//            return "/exhibit/items"
//
//        }
//    }
//
//    public var method: Moya.Method {
//        switch self {
//
//        case .getItems,
//             .getItem:
//            return .get
//
//        case .createItem:
//            return .post
//
//        default:
//            return .get
//
//        }
//    }
//
//    public var parameters: [String: Any]? {
//        switch self {
//
//        case .createItem(let name, let description, let image_url, let price, let deadline, let status, let username):
//            return [
//                "name" : name,
//                "description" : description,
//                "image_url" : image_url,
//                "price" : price,
//                "deadline" : deadline,
//                "status" : status,
//                "username" : username ?? "",
//            ]
//
//        default:
//            return nil
//        }
//    }
//
//    var sampleData: Data {
//        return Data()
//    }
//}


struct Network {

    static let queue = DispatchQueue(label: "com.lipscosme.LIPS.request", attributes: DispatchQueue.Attributes.concurrent)

    #if DEBUG
    static let plugins: [PluginType] = [
        NetworkLoggerPlugin(verbose: true)
    ]
    #else
    static let plugins: [PluginType] = []
    #endif

    static let provider = MoyaProvider<DjangoAPI>(
        endpointClosure: { (target: DjangoAPI) -> Endpoint<DjangoAPI> in

            let errorSampleResponseClosure = { () -> EndpointSampleResponse in

                return .networkResponse(200, "{\"mesasage\": \"mesasage\"}".data(using: String.Encoding.utf8)!)
            }

            let endpoint: Endpoint<DjangoAPI> = Endpoint<DjangoAPI>(
                url: target.baseURL.absoluteString + target.path,
                sampleResponseClosure: errorSampleResponseClosure,
                method: target.method,
                task: target.task,
                httpHeaderFields: [:]
            )

            return endpoint
    },
        manager: manager,

        plugins: plugins
    )

    static let manager: Manager = {
        let configuration = URLSessionConfiguration.default
        configuration.httpAdditionalHeaders = Manager.defaultHTTPHeaders
        configuration.timeoutIntervalForRequest = 10.0
        return Manager(configuration: configuration)
    }()

    static func request(
        target: DjangoAPI,
        success successCallback: @escaping (_ json: JSON) -> Void,
        error errorCallback: @escaping (_ statusCode: Int) -> Void,
        failure failureCallback: @escaping (Moya.MoyaError) -> Void
        ) -> Cancellable
    {

        return provider.request(target, callbackQueue: self.queue) { result in

            switch result {

            case let .success(response):

                do {
                    let _ = try response.filterSuccessfulStatusCodes()
                    let json = try JSON(response.mapJSON())

                    successCallback(json)
                }
                catch _ {

                    if response.statusCode == 200 {

                        successCallback(JSON.null)
                    }

                    DispatchQueue.main.async {

                        errorCallback(response.statusCode)
                    }
                }

            case let .failure(error):

                DispatchQueue.main.async {

                    failureCallback(error)
                }
            }
        }
    }

}

