(function ($) {

    var Item = Backbone.Model.extend({
        defaults: {
            url: 'page',
            count: '0'
        }
    });

    var List = Backbone.Collection.extend({
        url: function(){
            return 'page/' + this.page;
        },
        model: Item,
        page: 1
    });

    var ListView = Backbone.View.extend({
        el: $('.table'),
        row_template: _.template('<tr><td><%= url %></td><td><%= count %></td></tr>'),

        initialize: function(){
            _.bindAll(this, 'render', 'appendRow');

            this.collection = new List();
            this.collection.bind("change reset add remove", this.appendRow, this);
            $('#getBtn').on('click', this.getPage);
            this.render();
        },

        render: function(){
            var self = this;
            $(this.el).empty();
            this.collection.sync('read', self.collection, {
                success: function (results){
                    self.collection.add(results);
                    $('#page').val(self.collection.page);
                }
            });
        },

        appendRow: function(item){
            $(this.el).append(this.row_template({
                count: item.get('count'),
                url: item.get('url')
            }));
        },

        getPage: function(){
            listView.collection.page = $('#page').val();
            listView.render();
        }

    });

    var listView = new ListView();
})(jQuery);