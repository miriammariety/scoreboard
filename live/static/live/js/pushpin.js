var container = $('.container');
var main = $('main');
var header = $('header');
var footer = $('footer');

main.css('padding-bottom', footer.outerHeight() + 'px');


$(window).on('scroll', function() {
    console.log($(window).scrollTop(), header.outerHeight(), header.find('.row').outerHeight());
    var height = header.outerHeight() - header.find('.row').outerHeight();
    if ($(window).scrollTop() > height) {
        header.addClass('mini');
        container.css('padding-top', header.outerHeight() + 'px');
    } else {
        header.removeClass('mini');
        container.removeAttr('style');
    }
});
