
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
	hyips: $resource(apiUrl + "/hyips/list", {}, {
      list: {
        method: "POST",
		url: apiUrl + "/hyips/list"
      },
	  listUnknow: {
        method: "POST",
		url: apiUrl + "/hyips/listUnknow"
      },
	  updateSite: {
        method: "POST",
		url: apiUrl + "/hyips/updateSite"
      },
	  updateMonitorSite: {
        method: "POST",
		url: apiUrl + "/hyips/updateMonitorSite"
      },
	  updateUnknowSite: {
        method: "POST",
		url: apiUrl + "/hyips/updateUnknowSite"
      },
	  create: {
        method: "POST",
		url: apiUrl + "/hyips/create"
      },
	  listSiteStats: {
        method: "POST",
		url: apiUrl + "/hyips/listSiteStats"
      },		  
    }),
  };
});