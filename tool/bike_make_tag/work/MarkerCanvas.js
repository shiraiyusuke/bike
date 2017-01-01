/**
 * Created by shirai on 2016/12/27.
 */
/*    HTML5 CANVAS Marker
 *  Ver1.1
 */
function MarkerCanvas(elm,imagesrc){
    this.index = 0;
    this.stack = [];
    if(elm) this.canvas = elm;
    else return;
    this.ctx = this.canvas.getContext('2d');

    this.image = new Image();
    this.image.src = imagesrc + "?" + new Date().getTime();
    this.image.addEventListener('load',this,false);

    var doc = elm.ownerDocument;
    doc.addEventListener("click",this,false);
    doc.defaultView.addEventListener("unload",this,false);

    this.handleEvent = function(event){
        switch (event.type){
            case 'load':this.imageload(event);return;
            case 'click':if(event.target === this.canvas)
                this.markeradd(event);
                return;
            case 'unload':this.finalize(event);return;
        }
    }

    this.imageload = function(event){
        this.ctx.drawImage(this.image,0,0,this.canvas.width,this.canvas.height);
        this.image.removeEventListener('load',this,true);
        this.image = null;
    }

    this.markeradd = function(event){
        var MarkerCanvasRect = event.target.getBoundingClientRect();
        var x = event.clientX - Math.floor(MarkerCanvasRect.left);
        var y = event.clientY - Math.floor(MarkerCanvasRect.top);
        this.stack[this.index] = this.ctx.getImageData(0,0,this.canvas.width,this.canvas.height);
        var text = (this.index + 1).toString(10);
        this.ctx.globalAlpha = 0.8;
        this.ctx.beginPath();
        this.ctx.arc(x,y,5,0,Math.PI*2,false);
        this.ctx.fillStyle = "red";
        this.ctx.fill();
        this.ctx.globalAlpha = 1.0;
        this.ctx.fillStyle = "blue";
        this.ctx.fillText(text,x - 1,y + 4,5);
        this.index += 1;
    }

    this.markerdel = function(index){
        if (index <= this.stack.length && index > 0){
            this.ctx.clearRect(0,0,this.canvas.width,this.canvas.height);
            this.ctx.putImageData(this.stack[index-1],0,0);
            for (var i= this.stack.length;i < index;i--){
                this.stack[i] = null;
            }
            this.index = index - 1;
        }else return;
    }

    this.finalize = function(){
        if(this.stack) this.stack.length = 0;
        this.canvas.removeEventListener("click",this,false);
        this.canvas.removeEventListener("unload",this,false);
        this.ctx = null;
        this.canvas = null;
    }

}

var myMarkerCanvas = new MarkerCanvas(document.getElementById("MarkerCanvas"),
    "/image/yahagi.png");

function markerdel(index){
    myMarkerCanvas.markerdel(index);
}
