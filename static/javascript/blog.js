$(document).ready(function(){
	$(".admin-remove").click(function(){
		var id = $('#post-id').val();
		$.get('/posts/'+id, {_method:'DELETE'},function(data){
			window.location.href = "/";
		});
	});
});