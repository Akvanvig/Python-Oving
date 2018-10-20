$(function() {
        console.log( "ready!" );
        $('.entry').on('click', function(){
                console.log( "Klikk" );
                var entry = this;
                var post_id = $(this).find('h3').attr('id');
                console.log(post_id);
                $.ajax({
                        type:'GET',
                        url: '/delete' + '/' + post_id,
                        context: entry,
                        success:function(result){
                                if(result['status'] === 1){
                                        $(this).remove();
                                }
                                console.log(result);
                        },
                        error:function(xhr, status, error) {
                                console.log("xhr: " + xhr);
                                console.log("status: " + status);
                                console.log("error: " + error);
                        }
                });
                console.log("ferdig");
        });
});
