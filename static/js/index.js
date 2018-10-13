function follow(url, id, csrf_token){
    $.ajax
    ({ 
        url: url,
        type: 'post',
        data: {"csrfmiddlewaretoken": csrf_token},
        success: function(result)
        {
            $('#'+id).text(result);
        }
    });
}