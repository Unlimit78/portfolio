function openModal(i){
	document.getElementsByClassName('modal')[i].style.display = 'flex';
	document.getElementById('main').style.position = 'fixed';
	document.getElementById('main').style.backgroundColor = 'black';
	document.getElementById('main').style.opacity = 0.8;
	document.getElementById('main').style.height = '100%';


}
function closeModal(i){
	document.getElementsByClassName('modal')[i].style.display = 'none';
	document.getElementById('main').style.position = 'none';
	document.getElementById('main').style.backgroundColor = 'none';
	document.getElementById('main').style.opacity = 0;
	document.getElementById('main').style.height = 0;
	
}
function showHeader(){
	header = document.getElementById('main-header');
	if (header.className ==='show'){
		header.style.display = 'flex';
		header.className = 'burg';
	}
	else if(header.className === 'burg'){
		header.style.display = 'none';
		header.className = 'show';
	}
	
}
function showInfo(i){
	let v = document.getElementsByClassName('modal-detail')[i];
	if (v.classList.contains('disabled')){
		v.style.opacity = 0;
		v.classList.remove('disabled');
	}
	else{
		v.style.opacity = 0.7;
		v.classList.add('disabled');
	}
	

}

 


window.onload = function(e){
	
	let slides = document.querySelectorAll('.slider-element');
	
	let currentSlide = 0;
	
	let slideInterval = setInterval(function (e){
		slides[currentSlide].className = 'slider-element';
		
		currentSlide = (currentSlide+1)%slides.length;
		slides[currentSlide].className = 'slider-element active';
		

	},3000);
	
	let header = document.getElementById('main-header');
	window.addEventListener('scroll', function() {
		if(pageYOffset>500){
			header.style.backgroundColor = 'black';
		}
		else{
			header.style.backgroundColor = '';
		}
  		
	});
	let dropArea = document.getElementById('dropzone');
	
	['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  		dropArea.addEventListener(eventName, preventDefaults, false);});
	function preventDefaults (e) {
 		e.preventDefault()
  		e.stopPropagation()
	};
	['dragenter', 'dragover'].forEach(eventName => {
  		dropArea.addEventListener(eventName, highlight, false)
	});
	['dragleave', 'drop'].forEach(eventName => {
  		dropArea.addEventListener(eventName, unhighlight, false);

	})
	function highlight(e) {
  		dropArea.classList.add('highlight');
	};
	function unhighlight(e) {
  		dropArea.classList.remove('highlight');
	};
	dropArea.addEventListener('drop', handleDrop, false);
	function handleDrop(e) {
  		let dt = e.dataTransfer;
  		let files = dt.files;
  		handleFiles(files);
  	}
  	function handleFiles(files) {
  		([...files]).forEach(uploadFile)
	}
	function uploadFile(file) {

  	dropArea.style.border = '1px solid blue';

  	let ne = document.createElement('div');

  	let list = new DataTransfer();
  	if(document.getElementById('f').files[0]){
  		list.items.add(document.getElementById('f').files[0]);
	}

  	list.items.add(file);

  	document.getElementById('f').files =list.files;

  	ne.className = 'file-el';
  	ne.innerHTML = file.name;


  	dropArea.appendChild(ne);


}

	
};
