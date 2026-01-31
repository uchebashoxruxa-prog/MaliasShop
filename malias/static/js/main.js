(function ($) {
 "use strict";
 
/*----------------------------
 Data-Toggle Tooltip
------------------------------ */	

$('[data-toggle="tooltip"]').tooltip();
 
 /*----------------------------
 wow js active
------------------------------ */
 new WOW().init();
 
/*----------------------------
 jQuery MeanMenu
------------------------------ */
	jQuery('nav#mobile-menu').meanmenu();

/*----------------------------
 jQuery MeanMenu
------------------------------ */
	$('.dropdown-toggle').dropdown()

//---------------------------------------------
//Nivo slider
//---------------------------------------------
	$('#ensign-nivoslider').nivoSlider({
		autoplay: true,
		slices: 15,
		animSpeed: 500,
		pauseTime: 5000,
		directionNav: true,
		pauseOnHover: false,
	});
	 
 /*----------------------------
 Active-Hot-Deals
------------------------------ */  
  $(".active-hot-deals").owlCarousel({
      autoPlay: false, 
	  slideSpeed:2000,
	  pagination:true,
	  navigation:false,	  
      items : 1,
	  navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
	  itemsDesktop : [1169,1],
	  itemsTablet: [991,1],
	  itemsTabletSmall: [767,2],
	  itemsMobile : [479,1],
  });

/*----------------------------
 Active-Bestseller
------------------------------ */  
  $(".active-bestseller").owlCarousel({
      autoPlay: false, 
	  slideSpeed:2000,
	  pagination:false,
	  navigation:true,	  
      items : 1,
	  navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
	  itemsDesktop : [1169,1],
	  itemsTablet: [991,1],
	  itemsTabletSmall: [767,1],
	  itemsMobile : [479,1],
  });

/*----------------------------
 Active-Sidebar-Banner
------------------------------ */  
  $(".active-sidebar-banner").owlCarousel({
      autoPlay: true, 
	  slideSpeed:2000,
	  pagination:false,
	  navigation:false,	  
      items : 1,
	  transitionStyle : "fade",
	  itemsDesktop : [1169,1],
	  itemsTablet: [991,1],
	  itemsTabletSmall: [767,1],
	  itemsMobile : [479,1],
  });

/*----------------------------
 Active-Recent-Posts
------------------------------ */  
  $(".active-recent-posts").owlCarousel({
      autoPlay: false, 
	  slideSpeed:2000,
	  pagination:true,
	  navigation:false,	  
      items : 1,
	  itemsDesktop : [1169,1],
	  itemsTablet: [991,1],
	  itemsTabletSmall: [767,1],
	  itemsMobile : [479,1],
  });

 /*----------------------------
 Active-Product-Carosel
------------------------------ */   
  $(".active-product-carosel").owlCarousel({
      autoPlay: false, 
	  slideSpeed:2000,
	  pagination:false,
	  navigation:true,	  
      items : 4,
	  navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
	  itemsDesktop : [1169,3],
	  itemsTablet: [991,2],
	  itemsTabletSmall: [767,2],
	  itemsMobile : [479,1],	  
  });
  
 /*----------------------------
 Active-Small-Product
------------------------------ */   
  $(".active-small-product").owlCarousel({
      autoPlay: false, 
	  slideSpeed:2000,
	  pagination:false,
	  navigation:true,	  
      items : 3,
	  navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
	  itemsDesktop : [1169,2],
	  itemsTablet: [991,2],
	  itemsTabletSmall: [767,1],
	  itemsMobile : [479,1],	
  });

 /*----------------------------
 Active-Brand-Logo
------------------------------ */   
  $(".active-brand-logo").owlCarousel({
      autoPlay: false, 
	  slideSpeed:2000,
	  pagination:false,
	  navigation:true,	  
      items : 6,
	  navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
	  itemsDesktop : [1169,5],
	  itemsTablet: [991,4],
	  itemsTabletSmall: [767,2],
	  itemsMobile : [479,1],
  });

 /*----------------------------
 Active-Hot-Deals-Style-2
------------------------------ */  
  $(".active-hot-deals-style-2").owlCarousel({
      autoPlay: false, 
	  slideSpeed:2000,
	  pagination:false,
	  navigation:false,	  
      items : 5,
	  itemsDesktop : [1169,4],
	  itemsTablet: [991,3],
	  itemsTabletSmall: [767,2],
	  itemsMobile : [479,1],
  });

 /*----------------------------
 Active-Product-Carosel-style-2
------------------------------ */   
  $(".active-product-carosel-style-2").owlCarousel({
      autoPlay: false, 
	  slideSpeed:2000,
	  pagination:false,
	  navigation:true,	  
      items : 5,
	  navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
	  itemsDesktop : [1169,4],
	  itemsTablet: [991,3],
	  itemsTabletSmall: [767,2],
	  itemsMobile : [479,1],
  });

 /*----------------------------
 	Active-Recent-Posts-style-2
------------------------------  */  
  $(".active-recent-posts-style-2").owlCarousel({
      autoPlay: false, 
	  slideSpeed:2000,
	  pagination:false,
	  navigation:true,	  
      items : 4,
	  navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
	  itemsDesktop : [1169,4],
	  itemsTablet: [991,3],
	  itemsTabletSmall: [767,2],
	  itemsMobile : [479,1],
  });


/*--------------------------
	Category Menu
---------------------------- */	
	 $('.rx-parent').on('click', function(){
		$('.rx-child').slideToggle();
		$(this).toggleClass('rx-change');
		
	});

	$(".embed-responsive iframe").addClass("embed-responsive-item");
	$(".carousel-inner .item:first-child").addClass("active");
	
/*--------------------------
	category left menu
---------------------------- */	
	 $('.category-heading').on('click', function(){
	 $('.category-menu-list').slideToggle(300);
	});	  


/*---------------------
 countdown
--------------------- */
	$('[data-countdown]').each(function() {
	  var $this = $(this), finalDate = $(this).data('countdown');
	  $this.countdown(finalDate, function(event) {
		$this.html(event.strftime('<span class="cdown days"><span class="time-count">%-D</span> <p>Days</p></span> <span class="cdown hour"><span class="time-count">%-H</span> <p>Hour</p></span> <span class="cdown minutes"><span class="time-count">%M</span> <p>Min</p></span> <span class="cdown second"> <span><span class="time-count">%S</span> <p>Sec</p></span>'));
	  });
	});	


/*---------------------
 price slider
--------------------- */  
	$(function() {
	  $( "#slider-range" ).slider({
	   range: true,
	   min: 40,
	   max: 600,
	   values: [ 60, 570 ],
	   slide: function( event, ui ) {
		$( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
	   }
	  });
	  $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
	   " - $" + $( "#slider-range" ).slider( "values", 1 ) );
	});	


/*--------------------------
 scrollUp
---------------------------- */	
	$.scrollUp({
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    }); 	





 
})(jQuery);

$(document).ready(function() {
    const $mainContainer = $('#main-image-container');
    const $mainImage = $('#main-product-image');
    const $zoomLens = $('#zoom-lens');
    const $zoomWindow = $('#zoom-window');
    const $zoomImage = $('#zoom-image');
    const $thumbnails = $('.thumbnail-item');
    const $thumbnailLinks = $('.thumbnail-link');

    const zoomLevel = 2;
    const lensSize = 100;

    let isZoomActive = false;
    let currentImageIndex = 0;
    let totalImages = $thumbnails.length;

    function initZoom() {
        const img = new Image();
        img.onload = function() {
            const containerWidth = $mainContainer.width();
            const containerHeight = $mainContainer.height();
            const imgWidth = this.width;
            const imgHeight = this.height;

            const zoomWidth = imgWidth * zoomLevel;
            const zoomHeight = imgHeight * zoomLevel;

            $zoomImage.css({
                width: zoomWidth + 'px',
                height: zoomHeight + 'px'
            });

            isZoomActive = true;
        };
        img.src = $mainImage.attr('src');
    }

    function loadImage(imageSrc) {
        $mainImage.css('opacity', '0.5');

        const img = new Image();
        img.onload = function() {
            $mainImage.attr('src', imageSrc);
            $mainImage.css('opacity', '1');

            $zoomImage.attr('src', imageSrc);

            setTimeout(initZoom, 100);
        };

        img.onerror = function() {
            $mainImage.css('opacity', '1');
            console.error('Image loading error:', imageSrc);
        };

        img.src = imageSrc;
    }

    function setActiveThumbnail(index) {
        $thumbnails.removeClass('active');
        $thumbnails.eq(index).addClass('active');
        currentImageIndex = index;
    }

    $mainContainer.on('mousemove', function(e) {
        if (!isZoomActive) return;

        const containerOffset = $mainContainer.offset();
        const containerWidth = $mainContainer.width();
        const containerHeight = $mainContainer.height();

        let mouseX = e.pageX - containerOffset.left;
        let mouseY = e.pageY - containerOffset.top;

        let lensX = mouseX - lensSize / 2;
        let lensY = mouseY - lensSize / 2;

        if (lensX < 0) lensX = 0;
        if (lensY < 0) lensY = 0;
        if (lensX > containerWidth - lensSize) lensX = containerWidth - lensSize;
        if (lensY > containerHeight - lensSize) lensY = containerHeight - lensSize;

        $zoomLens.css({
            left: lensX + 'px',
            top: lensY + 'px',
            display: 'block'
        });

        $zoomWindow.addClass('show');

        const ratioX = lensX / (containerWidth - lensSize);
        const ratioY = lensY / (containerHeight - lensSize);

        const zoomImgWidth = $zoomImage.width();
        const zoomImgHeight = $zoomImage.height();
        const zoomWindowWidth = $zoomWindow.width();
        const zoomWindowHeight = $zoomWindow.height();

        const moveX = Math.max(0, (zoomImgWidth - zoomWindowWidth) * ratioX);
        const moveY = Math.max(0, (zoomImgHeight - zoomWindowHeight) * ratioY);

        $zoomImage.css({
            left: -moveX + 'px',
            top: -moveY + 'px'
        });
    });

    $mainContainer.on('mouseleave', function() {
        $zoomLens.hide();
        $zoomWindow.removeClass('show');
    });

    $thumbnailLinks.on('click', function(e) {
        e.preventDefault();

        const $this = $(this);
        const imageSrc = $this.data('image-src');
        const $thumbnailItem = $this.closest('.thumbnail-item');
        const index = $thumbnailItem.data('image-index');

        loadImage(imageSrc);

        setActiveThumbnail(index);
    });

    $('#btn-next').on('click', function() {
        let nextIndex = currentImageIndex + 1;
        if (nextIndex >= totalImages) nextIndex = 0;

        const imageSrc = $thumbnails.eq(nextIndex).find('.thumbnail-link').data('image-src');
        loadImage(imageSrc);
        setActiveThumbnail(nextIndex);
    });

    $('#btn-prev').on('click', function() {
        let prevIndex = currentImageIndex - 1;
        if (prevIndex < 0) prevIndex = totalImages - 1;

        const imageSrc = $thumbnails.eq(prevIndex).find('.thumbnail-link').data('image-src');
        loadImage(imageSrc);
        setActiveThumbnail(prevIndex);
    });

    function preloadImages() {
        $thumbnailLinks.each(function() {
            const img = new Image();
            img.src = $(this).data('image-src');
        });
    }

    $(window).on('resize', function() {
        initZoom();
    });

    initZoom();
    preloadImages();

    if ($(window).width() < 768) {
        $mainImage.on('click', function() {
            $zoomWindow.toggleClass('show');
        });

        $mainContainer.off('mousemove');
    }
});