(function($) {


    var NewsModel = Backbone.Model.extend({});
    var NewsCollection = Backbone.Collection.extend({
        model: NewsModel,
        url: function() {
            return '/search?' + $('.my-input').serialize();
        }
    });

    var NewsView = Backbone.View.extend({
        el: $('body'),

        events: {
            "click .my-button": "search"
        },

        initialize: function() {
            var expanded = false;
            _.bindAll(this, 'render', 'togglePanels', 'listNews')
            this.collection = new NewsCollection();
            this.collection.bind("add", this.render);
        },
        render: function() {
            if (!this.expanded) {
                this.togglePanels();
                $("ul.search-list").addClass("highlight-list");
                this.expanded = true;
            }
            this.listNews();
        },
        togglePanels: function() {
            $(".sidebar").toggleClass("sidebar-center sidebar-right pure-u-1 pure-u-1-4");
            $(".my-title").toggleClass("my-title-center my-title-right");
            $(".my-form").toggleClass("my-form-center my-form-right");
            $(".my-input").toggleClass("my-input-center my-input-right");
            $(".my-button").toggleClass("my-button-center my-button-right");
        },
        listNews: function() {
            $(".content").empty();
            var template = $("#news-template").html();
            var compiled = _.template(template);
            console.log( this.collection.toJSON());
            var content = compiled({items: this.collection.models});
            $(".content").html(content);
        },
        search: function() {
            this.collection.fetch();
        }


    });




    var newsView = new NewsView();

})(jQuery);
