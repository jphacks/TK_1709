import Foundation

class ImagesService: NSObject {
    
    func post(image: String, completion: ((Any?) -> Void)?) {
        
        _ = Network.request(
            target: .sendImage(img: image),
            success: { json in
                if let images = json.arrayValue.first?.dictionaryObject {
                    completion?(images["file_urls"])
                }
        },
            error: { statusCode in
        },
            failure: { error in
        })
    }
}
