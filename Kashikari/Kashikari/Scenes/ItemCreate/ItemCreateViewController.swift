import Foundation
import UIKit

class ItemCreateViewController: UIViewController {
    var items: [Item] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        navigationController?.navigationBar.isTranslucent = false
        view.backgroundColor = UIColor.defaultBackGroundColor
        setupViews()
    }

    func setupViews() {

    }
}

