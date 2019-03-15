function funcopen(url) {

    val =  ' <video id="video1" autoplay width="600" height="100" controls><source src="'+url+'"type="audio/mpeg"> </video>'

    $('#vv').html(val)
     myVid=document.getElementById("video1");
    myVid.volume=0.3;
}

function funcollection(id) {
    $.get('collection','id='+id,function (data) {
        alert(data['data'])
    })
}


function funsearch() {
    var s = $('#ser').val()

    $.get('search','key='+s,function (data) {
        var songs = data['result']['songs']
        var val = ''
        $.each(songs,function (i,t) {

            var id = t['id']
            var link = 'http://music.163.com/song/media/outer/url?id='+id+'.mp3'

            val+="<tr>"
            val+="<td>"+t['name']+"</td>"
            val+="<td>"+t['artists'][0]['name']+"</td>"
            val+="<td>"+0+"</td>"
           val+="<td><button onclick=" +  "'funcollection(" + '"'   +id +'"' +")'" +">收藏</button></td>"
            val+="<td><button onclick=" +  "'funcopen(" + '"'   +link +'"' +")'" +">播放</button></td>"
            val+="</tr>"

        })
         $('tbody').html(val)
    },'json')
}