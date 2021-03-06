
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
	talks: $resource(apiUrl + "/talks/list", {}, {
      list: {
        method: "POST",
		url: apiUrl + "/talks/list"
      },
	  listLesson: {
        method: "POST",
		url: apiUrl + "/talks/listLesson"
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
	hyips2: $resource(apiUrl + "/hyips/list2", {}, {
      list: {
        method: "POST",
		url: apiUrl + "/hyips/list2"
      },
	  listSiteInvest : {
        method: "POST",
		url: apiUrl + "/hyips/listSiteInvest"
      },
	  createInvest : {
        method: "POST",
		url: apiUrl + "/hyips/createInvest"
      },
	  updateInvest : {
        method: "POST",
		url: apiUrl + "/hyips/updateInvest"
      },
	  deleteInvest : {
        method: "POST",
		url: apiUrl + "/hyips/deleteInvest"
      }
    }),
	accounts: $resource(apiUrl + "/account/list", {}, {
      list: {
        method: "POST",
		url: apiUrl + "/accounts/list"
      },	  
	  create : {
        method: "POST",
		url: apiUrl + "/accounts/create"
      },
	  update : {
        method: "POST",
		url: apiUrl + "/accounts/update"
      }
    }),
	stats: $resource(apiUrl + "/stats/listRcb", {}, {
      listRcb: {
        method: "POST",
		url: apiUrl + "/stats/listRcb"
      },
	  listRcbTotal: {
        method: "POST",
		url: apiUrl + "/stats/listRcbTotal"
      }
    }),
  };
});