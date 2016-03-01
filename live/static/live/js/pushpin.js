var headers = $('.headers')
$(document).on('scroll', function() {
	if (window.scrollY > headers.height()) {
		headers.addClass('pinned-headers');
	} else {
		headers.removeClass('pinned-headers');
	}
});
