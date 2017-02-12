import re


html = """
    <div class="reveal">
        <div class="markdown slides"></div>
    </div>
    <script src="../bin/jquery.min.js"></script>
    <script src="../bin/marked-reveal.min.js"></script>
    <script>
        $("div.markdown").html("<section>"+marked($("textarea.markdown").val())+"</section>")
    </script>
    <script src="../reveal/js/reveal.js"></script>
    <script>
        Reveal.initialize({
            slideNumber: true,
            history: true,
            mouseWheel: true,
            transition: "slide"
        })
    </script>
</body>
</html>
"""

javascript = re.sub(r"\"", r"'", html)
javascript = re.sub(r"\.\./", r"", javascript)
javascript = re.sub(r"\n", r"\\\n", javascript)
javascript = re.sub(r"""<script""", r"""<scr"+"ipt""", javascript)
javascript = re.sub(r"""</script""", r"""</scr"+"ipt""", javascript)
print
print """document.writeln(\"""",
print javascript,
print """")"""