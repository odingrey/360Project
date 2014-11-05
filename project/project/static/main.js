$( document ).ready(function(){	
	$('li img').on('click',function(){
		if ($(this).hasClass('main_image')){
			var src = $(this).attr('src');
			var img = '<img id = "focused_image" src="' + src + '" class="img-responsive"/>';
			$('#imageModal').attr('source', $(this).attr('src'));
			$('#imageModal').attr('image_id', $(this).attr('id'));
			$('#imageModal').modal();
			$('#imageModal').on('shown.bs.modal', function(){
				$('#imageModal .modal-body').html(img);
			});
			$('#imageModal').on('hidden.bs.modal', function(){
				$('#imageModal .modal-body').html('');
			});
			$('#file-name').html('<center><h2>' + $(this).attr('id') + '</h2></center>');
		}
	});
});
function save_change(csrf){
	var brightness = $('#brightness_slider').val();
	var src = $('#imageModal').attr('source');
	var image_id = $('#imageModal').attr('image_id');
	$.post("/slowergram/edit/", { 
		'brightness' : brightness,
		'src' : src,
		csrfmiddlewaretoken: csrf
	}, function(){
		d = new Date();
		$( image_id ).attr('src', src + "?timestamp=" +d.getTime());
		$( '.modal' ).modal('hide');
		$( '#main' ).load( '/slowergram/main' );
	});
}
function update(brightness){
	var id = '#focused_image';	//TODO(mike): Rename this
	Caman(id, function () {
		this.brightness(brightness);
		this.render();
	});
}


function delete_image(csrf){
	var x;
	var name = $('#imageModal').attr('image_id');
	if (confirm("Are you sure you want to delete " + name) == true) {
	        var src = $('#imageModal').attr('source');
		$.post("/slowergram/delete/", {
			'src' : src,
			csrfmiddlewaretoken: csrf
	        }, function(){
			$( '.modal' ).modal('hide');
			//$( '#main' ).load( '/slowergram/main' );
			$( name ).parents('li').remove();
		});
	}
}
