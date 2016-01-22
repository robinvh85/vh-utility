
angular.module("app").factory("resources", function($resource) {
  var apiUrl, host;
  host = "";
  apiUrl = host + "";
  return {
	words: $resource(apiUrl + "/words/list", {}, {
      list: {
        method: "POST",
		url: apiUrl + "/words/list"
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