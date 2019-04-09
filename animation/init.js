requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        var io = new extIO({
            animation: function($expl, data){
                if (!data.ext || !data.ext.explanation) {
                    return;
                }
                var expl = data.ext.explanation;
                $expl.addClass('output').html(expl);
            },
            animationTemplateName: 'animation',
            multipleArguments: true,

            tryit: function(this_e){
                $tryit = this_e.extSetHtmlTryIt(this_e.getTemplate('tryit'));

                var tryitTextInput = $tryit.find('.tryit_text_input');
                var tryitWordsInput = $tryit.find('.tryit_words_input');
                tryitTextInput.focus();

                $tryit.find('.bn-check').click(function (e) {
                    var tryitTextData = tryitTextInput.val();
                    var tryitWordsData = tryitWordsInput.val().split(/[\s,]+/);
                    this_e.extSendToConsoleCheckiO(tryitTextData, tryitWordsData);
                    e.stopPropagation();
                    return false;
                });
            },
            retConsole: function (ret) {
                $tryit.find('.checkio_result').html("Your result:<br>" + ret);
            },

            functions: {
                js: 'countWords',
                python: 'count_words'
            }
        });
        io.start();
    }
);
