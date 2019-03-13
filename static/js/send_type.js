$('.row img').click(
    function () {

    $.get('type','type='+this.name,function (datas) {


        myeach(datas)



var tf = '<tr>'

   for(var i=1;i<datas['nums']*1+1;i++){

          tf+='<td><button  onclick=' +"funcpage(" +i+","+"'"+datas['type']+"'" + ")>"+i+"</button></td>>"
   }
   tf+='</tr>'


      $('.pages').html(tf)
    },'json')
    }
)


function funcpage(id,type) {
   $.get('type','type='+type+'&id='+id,function (datas) {
            myeach(datas)
   },'json')
}


function myeach(datas) {
    var val = ''
    $.each(datas['data'],function (i,t) {
            val+="<tr>"
            val+="<td>"+t[0]+"</td>"
            val+="<td>"+t[1]+"</td>"
            val+="<td>"+t[2]+"</td>"
            val+="<td><button id ='"+t[3]+"'>收藏</button>"
            val+="<td><a href='"+t[4]+"'>播放</a></td>"
            val+="</tr>"
        })
    $('tbody').html(val)
}