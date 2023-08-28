function setup() {
	createCanvas(windowWidth, windowHeight);
	background("white");
	sliderN = createSlider(0, 100, 5);
	sliderN.position(10, 10);
  sliderN.style('width', '300px');
	sliderR = createSlider(0, 1000, 100);
	sliderR.position(10, 30);
  sliderR.style('width', '400px');
}

function drawP(x, y, r, n){
	textSize(0.1*r);
	clear();
	let a = 2*PI/n;
	let xp = [];
	let yp = [];
	
	for(i=0; i<n;i++){
		append(xp, x+r*cos(i*a-PI/2));
		append(yp, y+r*sin(i*a-PI/2));
		
	}
	
	for(i=0; i<n;i++){
		for(j=0; j<n;j++){
			line(xp[i], yp[i], xp[j], yp[j]);
			
		}
	}
	for(i=0; i<n;i++){
		fill(150);
		circle(xp[i], yp[i], 0.2*r);
		fill(0);
		text(i, xp[i]-(i<10?0.025:0.05)*r, yp[i]-0.05*r,0.4*r, 0.4*r);
	}
	text(n*(n-1)/2, 10, 60);
	text(n, 10, 100);
	
}
function draw() {
	
	drawP(1000, 500, sliderR.value(), sliderN.value());
}
