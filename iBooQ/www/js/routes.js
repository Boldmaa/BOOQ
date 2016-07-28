angular.module('app.routes', [])

.config(function($stateProvider, $urlRouterProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $stateProvider
    
  

      .state('tabsController.booQ', {
    url: '/home',
    views: {
      'tab1': {
        templateUrl: 'templates/booQ.html',
        controller: 'booQCtrl'
      }
    }
  })

  .state('tabsController.cloudTabDefaultPage', {
    url: '/page4',
    views: {
      'tab3': {
        templateUrl: 'templates/cloudTabDefaultPage.html',
        controller: 'cloudTabDefaultPageCtrl'
      }
    }
  })

  .state('tabsController', {
    url: '/tabs',
    templateUrl: 'templates/tabsController.html',
    abstract:true
  })

  .state('login', {
    url: '/login',
    templateUrl: 'templates/login.html',
    controller: 'loginCtrl'
  })

  .state('signup', {
    url: '/signup',
    templateUrl: 'templates/signup.html',
    controller: 'signupCtrl'
  })

  .state('tabsController.tohiroo', {
    url: '/tohiroo',
    views: {
      'tab6': {
        templateUrl: 'templates/tohiroo.html',
        controller: 'tohirooCtrl'
      }
    }
  })

  .state('tabsController.zar-nemeh', {
    url: '/zar_nemeh',
    views: {
      'tab5': {
        templateUrl: 'templates/zar-nemeh.html',
        controller: 'zar-nemehCtrl'
      }
    }
  })

  .state('tabsController.huseltuud', {
    url: '/huseltuud',
    views: {
      'tab2': {
        templateUrl: 'templates/huseltuud.html',
        controller: 'huseltuudCtrl'
      }
    }
  })

  .state('tabsController.zarlal', {
    url: '/zarlal',
    views: {
      'tab1': {
        templateUrl: 'templates/zarlal.html',
        controller: 'zarlalCtrl'
      }
    }
  })

  .state('tabsController.tohiroo-delgerengui', {
    url: '/tohiroo-delgerengui',
    views: {
      'tab6': {
        templateUrl: 'templates/tohiroo-delgerengui.html',
        controller: 'tohiroo-delgerenguiCtrl'
      }
    }
  })

  .state('hereglegch', {
    url: '/hereglegch',
    templateUrl: 'templates/hereglegch.html',
    controller: 'hereglegchCtrl'
  })

  .state('tohirgoo', {
    url: '/tohirgoo',
    templateUrl: 'templates/tohirgoo.html',
    controller: 'tohirgooCtrl'
  })

  .state('nuuts_ug_solih', {
    url: '/nuuts_ug_solih',
    templateUrl: 'templates/nuuts_ug_solih.html',
    controller: 'nuuts_ug_solihCtrl'
  })

$urlRouterProvider.otherwise('/tabs/home')

  

});