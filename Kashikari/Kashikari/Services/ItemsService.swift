import UIKit

import SwiftyJSON
import ObjectMapper

class ItemsService: NSObject {

    func index(completion: (([Item]) -> Void)?) {
        
        _ = Network.request(
            target: .getItems,
            success: { json in
                let items: [Item] = Mapper<Item>().mapArray(JSONArray: json.arrayValue.map({ $0.dictionaryObject! }))
                completion?(items)
        },
            error: { statusCode in
        },
            failure: { error in
        })
    }
}
