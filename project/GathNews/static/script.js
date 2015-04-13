(function ($) {

    var News = Backbone.Model.extend({
        defaults: {
            title: '',
            link: ''
        }
    });

    var NewsList = Backbone.Collection.extend({

        model: News,
        url: '/search'
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
                console.log("fuck")
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
            _(this.collection.models).each(function (item) {
                $('ul', self.el).append("<li><a href="+ item.get("link")+">"+item.get("title") + "</a></li>");
            });
        }

    });
    var newsView = new NewsView();
})(jQuery);
