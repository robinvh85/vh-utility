
angular.module("app").factory("resources", function($resource) {
  var apiUrl, host;
  host = "";
  apiUrl = host + "";
  return {
    index: $resource(apiUrl + "/index", {}, {
      get: {
        method: "GET",
		url: apiUrl + "/index/list"
      },
    })
  };
});