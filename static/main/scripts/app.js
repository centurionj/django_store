(function ($) {
  "use strict";

  var fn = {

    // Launch Functions
    Launch: function () {
      fn.OwlCarousel();
      fn.ImageView();
      fn.Swiper();
      fn.Apps();
    },

    // owlcarousel
    OwlCarousel: function() {

      $('.owl-carousel').each(function() {
        var a = $(this),
          navid = a.data('id'),
          items = a.data('items') || [1,1,1,1],
          margin = a.data('margin'),
          loop = a.data('loop'),
          nav = a.data('nav'),
          dots = a.data('dots'),
          center = a.data('center'),
          speed = a.data('speed'),
          autoplay = a.data('autoplay'),
          autoplayTimeout = a.data('autoplaytimeout'),
          autoplaySpeed = a.data('autoplayspeed'),
          rtl = a.data('rtl'),
          autoheight = a.data('autoheight'),
          mouse = a.data('mouse'),
          thumbs = a.data('thumbs');

        var options = {
          nav: nav || false,
          loop: loop || false,
          dots: dots || false,
          center: center || false,
          autoplay: autoplay || false,
          autoHeight: autoheight || false,
          rtl: rtl || false,
          margin: margin || 0,
          navSpeed: speed || 400,
          dotsSpeed: speed || 400,
          autoplayTimeout: autoplayTimeout || 3000,
          autoplaySpeed: autoplaySpeed || 400,
          autoplayHoverPause: false,
          thumbs: thumbs || false,
          thumbsPrerendered: thumbs || false,
          navContainer: navid || false,
          mouseDrag: mouse || true,
          responsive: {
            0: { items: items[3] || 1 },
            768: { items: items[2] || 1 },
            1200: { items: items[1] || 1 },
            1600: { items: items[0] || 1}
          }
        };

        a.owlCarousel(options);
      });
    },


    // image view
    ImageView: function() {
      $('.lightbox').magnificPopup({
        type: 'image',
        closeOnContentClick: true,
        closeBtnInside: false,
        fixedContentPos: true,
        mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
        image: {
          verticalFit: true
        }
      });

      $('.gallery').each(function() { // the containers for all your galleries
          $(this).magnificPopup({
              delegate: 'figure > a', // the selector for gallery item
              type: 'image',
              mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
              gallery: {
                enabled:true
              }
          });
      });
    },


    // swiper
    Swiper: function() {

      $('.swiper-container').each(function(index, element){
        var $this = $(this)

        $this.find(".swiper-pagination").addClass("swiper-pagination-" + index);
        $this.find(".swiper-button-next").addClass("swiper-button-next-" + index);
        $this.find(".swiper-button-prev").addClass("swiper-button-prev-" + index);

        var options = {
          parallax: true,
          speed: 1000,
          simulateTouch: false,
          effect: 'fade',

          //pagination
          pagination: {
            el: '.swiper-pagination-' + index,
            clickable: true,
            type: 'fraction'
          },

          // navigation
          navigation: {
            nextEl: '.swiper-button-next-' + index,
            prevEl: '.swiper-button-prev-' + index,
          }

        };

        var slider = $(this);

        if ($(this).hasClass('swiper-container-carousel')) {
          options.spaceBetween = 10;
          options.effect = 'slide';
          options.simulateTouch = true;
          options.slideToClickedSlide = true;
        }

        new Swiper ( slider, options );
      });



      if ( $( ".gallery-container" ).length ) {
        var galleryTop = new Swiper('.gallery-container', {
          effect: 'fade',
          speed: 1500,
          simulateTouch: false
        });
        var galleryThumbs = new Swiper('.gallery-thumbs', {
          centeredSlides: true,
          slidesPerView: 6,
          speed: 1500,
          breakpoints: {
            1600: { slidesPerView: 5 },
            1200: { slidesPerView: 3 },
            768: { slidesPerView: 2 },
            576: { slidesPerView: 2 }
          },
          slideToClickedSlide: true
        });
        galleryTop.controller.control = galleryThumbs;
        galleryThumbs.controller.control = galleryTop;
      }

    },


    // apps
    Apps: function () {
      
      // lavalamp
      $('.lavalamp').lavalamp({
        setOnClick: true,
        enableHover: false,
        margins: false,
        autoUpdate: true,
        duration: 200
      });


      // select2 - custom select inputs
      $(document).ready(function() {
        $('body').find('select').each(function() {
          var dropdownParent = $(this).parent();
          
          $(this).select2({
            minimumResultsForSearch: -1,
            dropdownParent: dropdownParent
          });
        });
      });


      // range slider
      $('.rangeslider').each(function() {
        var a = $(this),
          min = a.data('min'),
          max = a.data('max'),
          from = a.data('from'),
          to = a.data('to')

        var options = {
          type: "double",
          min: min || 0,
          max: max || 1000,
          from: from || 200,
          to: to || 800,
          prefix: "$"
        };

        a.ionRangeSlider(options);
      });


      //  accordion with radio buttons
      $(".accordion-radio").on('click', function(){
          $(this).next('input').prop("checked", true);
      });

      // accordion active class
      $('.collapse').on('show.bs.collapse', function () {
        $(this).parent().addClass('active');
      });

      $('.collapse').on('hide.bs.collapse', function () {
        $(this).parent().removeClass('active');
      });


      // skrollr
      skrollr.init({
          forceHeight: false,        
          mobileCheck: function() {
              //hack - forces mobile version to be off
              return false;
          }
      });


      // filter blog
      $(function () {

        if ( $('.filtr-container').length ) {
          $('.imagesloaded').imagesLoaded( function() {

            var filterizdContainer = $('.filtr-container').filterizr({
              filter: '1',
              layout: 'packed'
            });

            $('a[data-filter]').click(function() {
              $('a[data-filter]').removeClass('active');
              $(this).addClass('active');
            });

          });
        }

        if ( $('.filtr-blog').length ) {
          $('.imagesloaded').imagesLoaded( function() {

            var filterizdBlog = $('.filtr-blog').filterizr({
              filter: 'all',
              layout: 'packed'
            });

            $('a[data-filter]').click(function() {
              $('a[data-filter]').removeClass('active');
              $(this).addClass('active');
            });

          });
        }

      });



      // tooltips
      $('[data-toggle="tooltip"]').tooltip();


      // smooth scroll
      $(function () {
        var scroll = new SmoothScroll('[data-scroll]');
      });

    }
  };

  $(document).ready(function () {
    fn.Launch();
  });

})(jQuery);