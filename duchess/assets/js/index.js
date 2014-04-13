$(function(){
    $('section.hero .buttons .start').click(function(){
        $('section.about').remove()
        $('section.hero').addClass('started');
        setTimeout(function(){$('section.hero video.intro').get(0).play();}, 2000);
    });
});
