
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
    }),
	words: $resource(apiUrl + "/words/list", {}, {
      get: {
        method: "GET"
      },
	  save: {
        method: "PUT",
        url: apiUrl + "/words/save"
      },
      create: {
        method: "POST",
        url: apiUrl + "/words/create"
      },
    }),
  };
});