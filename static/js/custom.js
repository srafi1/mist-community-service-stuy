
// NIVO LIGHTBOX
$('.iso-box-section a').nivoLightbox({
    effect: 'fadeScale',
});

// ISOTOPE FILTER
jQuery(document).ready(function($){

    if ( $('.iso-box-wrapper').length > 0 ) { 

	var $container 	= $('.iso-box-wrapper'), 
	$imgs 		= $('.iso-box img');



	$container.imagesLoaded(function () {

	    $container.isotope({
		layoutMode: 'fitRows',
		itemSelector: '.iso-box'
	    });

	    $imgs.load(function(){
	    	$container.isotope('reLayout');
	    })

	});

	//filter items on button click

	$('.filter-wrapper li a').click(function(){

	    var $this = $(this), filterValue = $this.attr('data-filter');

	    $container.isotope({ 
		filter: filterValue,
		animationOptions: { 
		    duration: 750, 
		    easing: 'linear', 
		    queue: false, 
		}              	 
	    });	            

	    // don't proceed if already selected 

	    if ( $this.hasClass('selected') ) { 
		return false; 
	    }

	    var filter_wrapper = $this.closest('.filter-wrapper');
	    filter_wrapper.find('.selected').removeClass('selected');
	    $this.addClass('selected');

	    return false;
	}); 

    }

});


// HIDE MOBILE MENU AFTER CLIKING ON A LINK
$('.navbar-collapse a').click(function(){
    $(".navbar-collapse").collapse('hide');
});


// SCROLLTO THE TOP
$(document).ready(function() {
    // Show or hide the sticky footer button
    $(window).scroll(function() {
	if ($(this).scrollTop() > 200) {
	    $('.go-top').fadeIn(200);
	} else {
	    $('.go-top').fadeOut(200);
	}
    });		
    // Animate the scroll to top
    $('.go-top').click(function(event) {
	event.preventDefault();
	
	$('html, body').animate({scrollTop: 0}, 300);
    })
});

// popup examples
$( document ).on( "pagecreate", function() {
    // The window width and height are decreased by 30 to take the tolerance of 15 pixels at each side into account
    function scale( width, height, padding, border ) {
	var scrWidth = $( window ).width() - 30,
	scrHeight = $( window ).height() - 30,
	ifrPadding = 2 * padding,
	ifrBorder = 2 * border,
	ifrWidth = width + ifrPadding + ifrBorder,
	ifrHeight = height + ifrPadding + ifrBorder,
	h, w;
	if ( ifrWidth < scrWidth && ifrHeight < scrHeight ) {
	    w = ifrWidth;
	    h = ifrHeight;
	} else if ( ( ifrWidth / scrWidth ) > ( ifrHeight / scrHeight ) ) {
	    w = scrWidth;
	    h = ( scrWidth / ifrWidth ) * ifrHeight;
	} else {
	    h = scrHeight;
	    w = ( scrHeight / ifrHeight ) * ifrWidth;
	}
	return {
	    'width': w - ( ifrPadding + ifrBorder ),
	    'height': h - ( ifrPadding + ifrBorder )
	};
    };
    $( ".ui-popup iframe" )
        .attr( "width", 0 )
        .attr( "height", "auto" );
    $( "#popupVideo" ).on({
	popupbeforeposition: function() {
	    // call our custom function scale() to get the width and height
	    var size = scale( 497, 298, 15, 1 ),
	    w = size.width,
	    h = size.height;
	    $( "#popupVideo iframe" )
		.attr( "width", w )
		.attr( "height", h );
	},
	popupafterclose: function() {
	    $( "#popupVideo iframe" )
		.attr( "width", 0 )
		.attr( "height", 0 );
	}
    });
});

function resizeFeedback() {
    var iframe = document.getEl
}
