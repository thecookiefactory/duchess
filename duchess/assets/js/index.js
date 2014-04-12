$(function(){
    $('section.hero .buttons .start').click(function(){
        $('section.hero').addClass('started');
        setTimeout(function(){$('section.hero video.intro').get(0).play();}, 2000);
    });
});
