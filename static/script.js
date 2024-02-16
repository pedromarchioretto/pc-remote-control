$('div').click(function(event){
  var id = this.id
  $.ajax({
    url: 'http://192.168.0.11:5000/',
    type: 'post',
    data: {service : id}
  })
})