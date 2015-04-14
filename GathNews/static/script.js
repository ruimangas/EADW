(function ($) {

    var News = Backbone.Model;

    var NewsList = Backbone.Collection.extend({

        model: News,
        url: '/search',

        parse: function (response) {
            return response.news
        }
    });



    var NewsView = Backbone.View.extend({
        el: $('body'),

        events: {
            'click button': 'search'
        },

        initialize: function () {
            var expanded = false; //indicates if the view is expanded
            _.bindAll(this, 'render', 'search', 'listNews');
            this.collection = new NewsList();
            this.collection.bind("add", this.render);
        },
        render: function () {
            var self = this;
            if (!this.expanded) {
                $("div.page-container").toggleClass("page-container page-container-expanded");
                $("ul.search-list").addClass("highlight-list");
                this.expanded = true;
            }
            this.listNews()
        },

        search : function () {
            this.collection.fetch();
        },

        listNews : function () {

            $("ul.search-list").empty();
            console.log(this.collection.models)
            _(this.collection.models).each(function (item) {
                $('ul', self.el).append("<li><a href="+ item.get("link")+">"+item.get("title") + "</a></li>");
            });
        }

    });
    var newsView = new NewsView();
})(jQuery);
