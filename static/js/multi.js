function funcopen(url) {

    val =  ' <video id="video1" autoplay width="600" height="100" controls><source src="'+url+'"type="audio/mpeg"> </video>'

    $('#vv').html(val)
     myVid=document.getElementById("video1");
    myVid.volume=0.3;
}

function funcollection(id,name,singer) {
    if (name){

        $.get('collection','id='+id+'&name='+name+"&singer="+singer,function (data) {
        alert(data['data'])
    })
    }else{
             $.get('collection','id='+id,function (data) {
        alert(data['data'])
    })

    }


}


function funsearch() {
    var s = $('#ser').val()

    $.get('search','key='+s,function (data) {
        var songs = data['result']['songs']
        var val = ''
        $.each(songs,function (i,t) {

            var id = t['id']
            var link = 'http://music.163.com/song/media/outer/url?id='+id+'.mp3'
            var name = t['name']//.replace("(","[")
            var sname = t['artists'][0]['name']//.replace("(",'[')

            val+="<tr>"
            val+="<td>"+name+"</td>"
            val+="<td>"+sname+"</td>"
            val+="<td>"+0+"</td>"
           //val+= "<td> <button onclick="+"funcollection("+"'"+id+"'"+","+"'"+t['name']+"'"+",'"+t['artists'][0]['name']+"'"+")>"+ "收藏"+ "</button></td>"
            val+="<td><button onclick="+  '"funcollection(' +"'"
            val+=id+"','"
            val+=name+"','"
            val+=sname+"'"+')">'
            val+="收藏"+"</button></td>"
            val+="<td><button onclick=" +  "'funcopen(" + '"'   +link +'"' +")'" +">播放</button></td>"
            val+="</tr>"

        })
         $('tbody').html(val)
    },'json')
}