import UIKit
import XLPagerTabStrip
import SnapKit

class MainViewController: ButtonBarPagerTabStripViewController {
    
    private lazy var logoImage: UIImageView = {
        let imageView = UIImageView(image: UIImage(named: "white_logo"))
        imageView.contentMode = .scaleToFill
        return imageView
    }()
    
    private lazy var cameraButton: UIButton = {
        let image = UIImage(named: "camera")
        let button = UIButton()
        button.setImage(image, for: .normal)
        button.addTarget(self, action: #selector(pushCameraAction), for: .touchUpInside)
        return button
    }()
    
    private lazy var actionSheet: UIAlertController = {
        let actionSheet: UIAlertController = UIAlertController(title:"画像を選択",
                                                               message: "投稿のための画像を選んでください(複数写っていても可)",
                                                               preferredStyle: .actionSheet)
        
        let cancelAction: UIAlertAction = UIAlertAction(title: "キャンセル",
                                                        style: .cancel,
                                                        handler:{
                                                            (action:UIAlertAction!) -> Void in
        })
        
        let cameraAction: UIAlertAction = UIAlertAction(title: "撮影",
                                                        style: .default,
                                                        handler:{ [weak self] (UIAlertAction) -> Void in
                                                            let vc = cameraViewController()
                                                            self?.navigationController?.pushViewController(vc, animated: true)
        })
        
        let libraryOpenAction: UIAlertAction = UIAlertAction(title: "ライブラリから選択",
                                                             style: .default,
                                                             handler:{ [weak self] (UIAlertAction) -> Void in
                                                                let ipc:UIImagePickerController = UIImagePickerController()
                                                                ipc.delegate = self
                                                                ipc.sourceType = .photoLibrary
                                                                self?.present(ipc, animated:true, completion:nil)
        })
        
        actionSheet.addAction(cancelAction)
        actionSheet.addAction(cameraAction)
        actionSheet.addAction(libraryOpenAction)
        return actionSheet
    }()
    
    @objc func pushCameraAction(){
        present(actionSheet, animated: true, completion: nil)
    }
    
    override func viewDidLoad() {
        setupTabs()
        super.viewDidLoad()
        _ = actionSheet
        view.backgroundColor = UIColor.white
        navigationItem.titleView = logoImage
        navigationItem.rightBarButtonItem = UIBarButtonItem(customView: cameraButton)
        navigationController?.navigationBar.isTranslucent = false
    }

    override func viewControllers(for pagerTabStripController: PagerTabStripViewController) -> [UIViewController] {
        var viewControllers: [UIViewController] = []
        for i in 0...(TabType.count - 1) {
            let vc = TabPageViewController()
            vc.tabType = TabType.create(rawValue: i)
            viewControllers.append(vc)
        }
        return viewControllers
    }
        
    private func setupTabs() {
        settings.style.buttonBarBackgroundColor = UIColor.white
        settings.style.buttonBarItemBackgroundColor = UIColor.white
        settings.style.selectedBarBackgroundColor = UIColor.themeColor
        settings.style.selectedBarHeight = 5
        settings.style.buttonBarItemFont = UIFont.boldSystemFont(ofSize: 13)
        settings.style.buttonBarItemTitleColor = UIColor.darkGray
        settings.style.buttonBarItemsShouldFillAvailiableWidth = true
        
        changeCurrentIndexProgressive = { (oldCell: ButtonBarViewCell?, newCell: ButtonBarViewCell?, progressPercentage: CGFloat, changeCurrentIndex: Bool, animated: Bool) -> Void in
            guard changeCurrentIndex == true else { return }
            oldCell?.label.textColor = UIColor.darkGray
            oldCell?.label.font = UIFont(name: UIFont.themeFont, size: 12)
            newCell?.label.textColor = UIColor.themeColor
            newCell?.label.font = UIFont(name: UIFont.themeBoldFont, size: 12)
        }
    }
}

extension MainViewController: UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : Any]) {
//        if let image = info[UIImagePickerControllerOriginalImage] as? UIImage, let imageData = UIImagePNGRepresentation(image) {
//            Service.images.post(image: imageData.base64EncodedString(), completion: {[weak self] images in
//                print(images!)
//            })
            
            let urls = ["https://static-mercari-jp-imgtr2.akamaized.net/photos/m61079367510_1.jpg?1509117582",
                        "https://static-mercari-jp-imgtr2.akamaized.net/photos/m623571634_1.jpg?1456582097",
                        "https://static-mercari-jp-imgtr2.akamaized.net/photos/m59616650679_1.jpg?1505530473"]
            
            let vc = ItemSelectViewController()
            vc.imageUrls = urls
            picker.pushViewController(vc, animated: true)
//        }
    }
}

