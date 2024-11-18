import io


class HappyDoc:
    def __init__(self):
        self.doc = io.StringIO()

    def __call__(self):
        return self.doc

    def render(self):
        res = self.doc.getvalue()
        self.doc.close()
        return res

    def write(self, text: str):
        self.doc.write(text)


class HTMLTag:
    __name__ = "htmltag"

    def __init__(self, _s=None, *, classes=None, id=None, **kwargs) -> None:
        if classes:
            kwargs["class"] = classes
        if id:
            kwargs["id"] = id

        self.tag_attrs = kwargs
        self.output = _s

    def _format_attributes(self) -> str:
        return " ".join(f'{key}="{value}"' for key, value in self.tag_attrs.items())


class HTMLContainerTag(HTMLTag):
    def __enter__(self) -> None:
        self.output.write(f"<{self.__name__} {self._format_attributes()}>")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.output.write(f"</{self.__name__}>")


class HTMLSelfClosingTag(HTMLTag):
    def __init__(self, _s=None, *, classes=None, id=None, **kwargs) -> None:
        super().__init__(_s=_s, classes=classes, id=id, **kwargs)
        self.output.write(f"<{self.__name__} {self._format_attributes()}/>")


################################################################################
# Tags are in alphabetic order
################################################################################


class a(HTMLContainerTag):
    __name__ = "a"


class abbr(HTMLContainerTag):
    __name__ = "abbr"


class acronym(HTMLContainerTag):
    __name__ = "acronym"


class address(HTMLContainerTag):
    __name__ = "address"


class area(HTMLSelfClosingTag):
    __name__ = "area"


class article(HTMLContainerTag):
    __name__ = "article"


class aside(HTMLContainerTag):
    __name__ = "aside"


class b(HTMLContainerTag):
    __name__ = "b"


class base(HTMLSelfClosingTag):
    __name__ = "base"


class bdi(HTMLContainerTag):
    __name__ = "bdi"


class bdo(HTMLContainerTag):
    __name__ = "bdo"


class blockquote(HTMLContainerTag):
    __name__ = "blockquote"


class body(HTMLContainerTag):
    __name__ = "body"


class br(HTMLSelfClosingTag):
    __name__ = "br"


class button(HTMLContainerTag):
    __name__ = "button"


class canvas(HTMLContainerTag):
    __name__ = "canvas"


class caption(HTMLContainerTag):
    __name__ = "caption"


class cite(HTMLContainerTag):
    __name__ = "cite"


class code(HTMLContainerTag):
    __name__ = "code"


class col(HTMLSelfClosingTag):
    __name__ = "col"


class colgroup(HTMLContainerTag):
    __name__ = "colgroup"


class data(HTMLContainerTag):
    __name__ = "data"


class datalist(HTMLContainerTag):
    __name__ = "datalist"


class dd(HTMLContainerTag):
    __name__ = "dd"


class del_(HTMLContainerTag):
    __name__ = "del"


class details(HTMLContainerTag):
    __name__ = "details"


class dfn(HTMLContainerTag):
    __name__ = "dfn"


class dialog(HTMLContainerTag):
    __name__ = "dialog"


class div(HTMLContainerTag):
    __name__ = "div"


class dl(HTMLContainerTag):
    __name__ = "dl"


class dt(HTMLContainerTag):
    __name__ = "dt"


class em(HTMLContainerTag):
    __name__ = "em"


class embed(HTMLSelfClosingTag):
    __name__ = "embed"


class fieldset(HTMLContainerTag):
    __name__ = "fieldset"


class figcaption(HTMLContainerTag):
    __name__ = "figcaption"


class figure(HTMLContainerTag):
    __name__ = "figure"


class footer(HTMLContainerTag):
    __name__ = "footer"


class form(HTMLContainerTag):
    __name__ = "form"


class h1(HTMLContainerTag):
    __name__ = "h1"


class h2(HTMLContainerTag):
    __name__ = "h2"


class h3(HTMLContainerTag):
    __name__ = "h3"


class h4(HTMLContainerTag):
    __name__ = "h4"


class h5(HTMLContainerTag):
    __name__ = "h5"


class h6(HTMLContainerTag):
    __name__ = "h6"


class head(HTMLContainerTag):
    __name__ = "head"


class header(HTMLContainerTag):
    __name__ = "header"


class hr(HTMLSelfClosingTag):
    __name__ = "hr"


class html(HTMLContainerTag):
    __name__ = "html"


class i(HTMLContainerTag):
    __name__ = "i"


class iframe(HTMLContainerTag):
    __name__ = "iframe"


class img(HTMLSelfClosingTag):
    __name__ = "img"


class input(HTMLSelfClosingTag):
    __name__ = "input"


class ins(HTMLContainerTag):
    __name__ = "ins"


class kbd(HTMLContainerTag):
    __name__ = "kbd"


class label(HTMLContainerTag):
    __name__ = "label"


class legend(HTMLContainerTag):
    __name__ = "legend"


class link(HTMLSelfClosingTag):
    __name__ = "link"


class main(HTMLContainerTag):
    __name__ = "main"


class map(HTMLContainerTag):
    __name__ = "map"


class mark(HTMLContainerTag):
    __name__ = "mark"


class marquee(HTMLContainerTag):
    __name__ = "marquee"


class math(HTMLContainerTag):
    __name__ = "math"


class menu(HTMLContainerTag):
    __name__ = "menu"


class meta(HTMLSelfClosingTag):
    __name__ = "meta"


class meter(HTMLContainerTag):
    __name__ = "meter"


class nav(HTMLContainerTag):
    __name__ = "nav"


class noscript(HTMLContainerTag):
    __name__ = "noscript"


class object(HTMLContainerTag):
    __name__ = "object"


class ol(HTMLContainerTag):
    __name__ = "ol"


class optgroup(HTMLContainerTag):
    __name__ = "optgroup"


class option(HTMLSelfClosingTag):
    __name__ = "option"


class output(HTMLContainerTag):
    __name__ = "output"


class p(HTMLContainerTag):
    __name__ = "p"


class param(HTMLSelfClosingTag):
    __name__ = "param"


class picture(HTMLContainerTag):
    __name__ = "picture"


class pre(HTMLContainerTag):
    __name__ = "pre"


class progress(HTMLContainerTag):
    __name__ = "progress"


class q(HTMLContainerTag):
    __name__ = "q"


class rb(HTMLContainerTag):
    __name__ = "rb"


class rp(HTMLContainerTag):
    __name__ = "rp"


class rt(HTMLContainerTag):
    __name__ = "rt"


class ruby(HTMLContainerTag):
    __name__ = "ruby"


class s(HTMLContainerTag):
    __name__ = "s"


class samp(HTMLContainerTag):
    __name__ = "samp"


class script(HTMLContainerTag):
    __name__ = "script"


class section(HTMLContainerTag):
    __name__ = "section"


class select(HTMLContainerTag):
    __name__ = "select"


class slot(HTMLContainerTag):
    __name__ = "slot"


class small(HTMLContainerTag):
    __name__ = "small"


class source(HTMLSelfClosingTag):
    __name__ = "source"


class source(HTMLSelfClosingTag):
    __name__ = "source"


class span(HTMLContainerTag):
    __name__ = "span"


class strong(HTMLContainerTag):
    __name__ = "strong"


class style(HTMLContainerTag):
    __name__ = "style"


class sub(HTMLContainerTag):
    __name__ = "sub"


class summary(HTMLContainerTag):
    __name__ = "summary"


class sup(HTMLContainerTag):
    __name__ = "sup"


class svg(HTMLContainerTag):
    __name__ = "svg"


class table(HTMLContainerTag):
    __name__ = "table"


class tbody(HTMLContainerTag):
    __name__ = "tbody"


class td(HTMLContainerTag):
    __name__ = "td"


class template(HTMLContainerTag):
    __name__ = "template"


class textarea(HTMLContainerTag):
    __name__ = "textarea"


class tfoot(HTMLContainerTag):
    __name__ = "tfoot"


class th(HTMLContainerTag):
    __name__ = "th"


class thead(HTMLContainerTag):
    __name__ = "thead"


class time(HTMLContainerTag):
    __name__ = "time"


class title(HTMLContainerTag):
    __name__ = "title"


class tr(HTMLContainerTag):
    __name__ = "tr"


class track(HTMLSelfClosingTag):
    __name__ = "track"


class u(HTMLContainerTag):
    __name__ = "u"


class ul(HTMLContainerTag):
    __name__ = "ul"


class var(HTMLContainerTag):
    __name__ = "var"


class video(HTMLContainerTag):
    __name__ = "video"


class wbr(HTMLSelfClosingTag):
    __name__ = "wbr"
