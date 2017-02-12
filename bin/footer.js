document.writeln(" \
    <div class='reveal'>\
        <div class='markdown slides'></div>\
    </div>\
    <scr"+"ipt src='bin/jquery.min.js'></scr"+"ipt>\
    <scr"+"ipt src='bin/marked-reveal.min.js'></scr"+"ipt>\
    <scr"+"ipt>\
        $('div.markdown').html('<section>'+marked($('textarea.markdown').val())+'</section>')\
    </scr"+"ipt>\
    <scr"+"ipt src='reveal/js/reveal.js'></scr"+"ipt>\
    <scr"+"ipt>\
        Reveal.initialize({\
            slideNumber: true,\
            history: true,\
            mouseWheel: true,\
            transition: 'zoom'\
        })\
    </scr"+"ipt>\
</body>\
</html>\
")

// transition: none, fade, slide, convex, concave, zoom
