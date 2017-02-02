/*! light-blue - v3.3.0 - 2016-03-08 */
$(function() {
    function a() {
        $("#tooltip-enabled, #max-length").tooltip(), autosize($(".autogrow")), $(".selectpicker").selectpicker(), $("#wysiwyg").wysihtml5({
            html: !0,
            customTemplates: b,
            stylesheets: [],
            toolbar: {
                size: "sm btn-inverse"
            }
        }), $(".select2").each(function() {
            $(this).select2($(this).data())
        }), new Switchery(document.getElementById("checkbox-ios1")), new Switchery(document.getElementById("checkbox-ios2"), {
            color: $blue
        }), $("#datetimepicker1").datetimepicker({
            format: !1
        }), $("#datetimepicker2").datetimepicker({}), $("#colorpicker").colorpicker({
            color: "#999"
        }), $("#mask-phone").mask("(999) 999-9999"), $("#mask-date").mask("99-99-9999"), $("#mask-int-phone").mask("+999 999 999 999"), $("#mask-time").mask("99:99"), $(".js-slider").slider(), $(".widget").widgster()
    }
    var b = {
        emphasis: function(a) {
            var b = (a.locale, a.options),
                c = b.toolbar && b.toolbar.size ? " btn-" + b.toolbar.size : "";
            return "<li><div class='btn-group'><a class='btn btn-default btn-" + c + "' data-wysihtml5-command='bold' title='CTRL+B' tabindex='-1'><i class='glyphicon glyphicon-bold'></i></a><a class='btn btn-default btn-" + c + "' data-wysihtml5-command='italic' title='CTRL+I' tabindex='-1'><i class='glyphicon glyphicon-italic'></i></a></div></li>"
        },
        link: function(a) {
            var b = (a.locale, a.options);
            b.toolbar && b.toolbar.size ? " btn-" + b.toolbar.size : "";
            return '<li><a class="btn btn-sm btn-inverse btn-default" data-wysihtml5-command="createLink" title="Insert link" tabindex="-1" href="javascript:;" unselectable="on">            <span class="glyphicon glyphicon-share"></span>            </a>            <div class="bootstrap-wysihtml5-insert-link-modal modal fade" data-wysihtml5-dialog="createLink">            <div class="modal-dialog ">                <div class="modal-content">                    <div class="modal-header">                        <a class="close" data-dismiss="modal">×</a>                        <h3>Insert link</h3>                    </div>                    <div class="modal-body">                        <div class="form-group no-margin">                            <input value="http://" class="bootstrap-wysihtml5-insert-link-url form-control bg-gray-lighter" data-wysihtml5-dialog-field="href" data-parsley-id="7677"><ul class="parsley-errors-list" id="parsley-id-7677"></ul>                            </div>                            <br>                            <div class="checkbox mt-sm checkbox-dark">                                <input type="checkbox" id="in-a-new-window" class="bootstrap-wysihtml5-insert-link-target" checked="">                                <label for="in-a-new-window">                                Open link in new window                                    </label>                                </div>                            </div>                            <div class="modal-footer">                                <a class="btn btn-default" data-dismiss="modal" data-wysihtml5-dialog-action="cancel" href="#">Cancel</a>                                <a href="#" class="btn btn-primary" data-dismiss="modal" data-wysihtml5-dialog-action="save">Insert link</a>                            </div>                        </div>                    </div>                </div></li>'
        },
        image: function(a) {
            return '<li><div class="bootstrap-wysihtml5-insert-image-modal modal fade" data-wysihtml5-dialog="insertImage" aria-hidden="true" style="display: none;">            <div class="modal-dialog ">                <div class="modal-content">                    <div class="modal-header">                        <a class="close" data-dismiss="modal">×</a>                        <h3>Insert image</h3>                    </div>                    <div class="modal-body">                        <div class="form-group no-margin">                            <input value="http://" class="bootstrap-wysihtml5-insert-image-url form-control bg-gray-lighter" data-parsley-id="7359"><ul class="parsley-errors-list" id="parsley-id-7359"></ul>                            </div>                        </div>                        <div class="modal-footer">                            <a class="btn btn-default" data-dismiss="modal" data-wysihtml5-dialog-action="cancel" href="#">Cancel</a>                            <a class="btn btn-primary" data-dismiss="modal" data-wysihtml5-dialog-action="save" href="#">Insert image</a>                        </div>                    </div>                </div>                </div>                <a class="btn btn-sm btn-inverse btn-default" data-wysihtml5-command="insertImage" title="Insert image" tabindex="-1" href="javascript:;" unselectable="on"><span class="glyphicon glyphicon-picture"></span></a>                </li>'
        },
        html: function(a) {
            var b = a.locale,
                c = a.options,
                d = c.toolbar && c.toolbar.size ? " btn-" + c.toolbar.size : "";
            return "<li><div class='btn-group'><a class='btn btn-default btn-" + d + "' data-wysihtml5-action='change_view' title='" + b.html.edit + "' tabindex='-1'><i class='fa fa-pencil'></i></a></div></li>"
        }
    };
    a(), PjaxApp.onPageLoad(a)
});