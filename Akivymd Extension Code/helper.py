KV = '''

<NavigationButton@Button_Item>
    icon_color: app.theme_cls.text_color
    text_color: 1, 1, 1, 1
    button_bg_color: app.theme_cls.primary_color
    mode: 'color_on_active'
    badge_disabled: True
    
MDScreen:
    MDBoxLayout:
        orientation: "vertical"
            
        MDToolbar:
            id: _toolbar
            title: 'vipin coding'
            left_action_items: [["menu", lambda x: app.callback()]]
            specific_text_color: 1, 1, 1, 1
        
        MDBoxLayout:
            AKBottomNavigation2:
                bg_color: app.theme_cls.bg_darkest
            
                NavigationButton:
                    text: 'Home'
                    icon: 'home-outline'
                                 
                                    
                NavigationButton:
                    text: 'Youtube'
                    icon: 'youtube'
            
                NavigationButton:
                    text: 'Notification'
                    icon: 'bell-outline'
                    
                NavigationButton:
                    text: 'Share'
                    icon: 'share-outline'
'''
