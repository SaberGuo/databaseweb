//task operations
var sign;

var updater = {
    poll: function(){
        $.ajax({url: "/task_start", 
                type: "POST", 
                dataType: "text",
                data:{'startingtask':$('td.startingtask').html()},
                success: updater.onSuccess,
                error: updater.onError});
    },
    onSuccess: function(data, dataStatus){
        try{
            $("td.taskdata").html(data);
        }
        catch(e){
            updater.onError();
            return;
        }
    },
    onError: function(){
        console.log("Poll error;");
    }
}

function start(){
    sign=window.setInterval(updater.poll, 4900);
    $.ajax({
      url:'/tasktime',
      type:'POST',
      dataType:'text',
      data:{'startingtask':$('td.startingtask').html(),
                'flag':0}
    });
    $('td.taskname').html($('td.startingtask').html());
    document.getElementById('delete_button').disabled=true;
}

function stop(){
    document.getElementById('delete_button').removeAttribute('disabled');
    window.clearInterval(sign);
    window.setTimeout(function(){
        $("td.taskname").html('undefined');
        $("td.taskdata").html('undefined');
    },1500);
    $.ajax({
      url:'/tasktime',
      type:'POST',
      dataType:'text',
      data:{'startingtask':$('td.startingtask').html(),
                'flag':1}
    });
    window.setTimeout(function(){
      window.location.href='/task';
    }, 1000)
}