$(document).ready(function(){
	$("#delete-confirm").hide();

	$(".admin-remove").click(function(){
		$("#delete-confirm").dialog("open");
	});
});

$(function(){
	var id = $("#post-id").val();
	$("#delete-confirm").dialog({
		resizable: false,
		autoOpen:false,
		height:250,
		width:400,
		modal:true,
		buttons : {
			"Yes?": function(){
				$.ajax({
					url:'/posts/' +id,
					method:'DELETE',
					success : function(result){
						$(".post").html(result);
					}
				});
				$(this).dialog("close");
			},
			Cancel : function(){
				$(this).dialog("close");
			}
		}
	});
});