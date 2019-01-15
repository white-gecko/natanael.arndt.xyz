import 'bootstrap';
import './main.scss';


var pdfjsLib = require('pdfjs-dist');

var pdfPath = 'https://arxiv.org/pdf/1805.03721';

// Setting worker path to worker bundle.
pdfjsLib.GlobalWorkerOptions.workerSrc =
  '../dist/pdf.worker.bundle.js';

// Loading a document.
var loadingTask = pdfjsLib.getDocument(pdfPath);
loadingTask.promise.then(function (pdfDocument) {
  // Request a first page
  return pdfDocument.getPage(1).then(function (pdfPage) {
    // Display page on the existing canvas with 100% scale.
    var viewport = pdfPage.getViewport({ scale: 1.0, });
    var canvas = document.getElementById('theCanvas');
    canvas.width = viewport.width;
    canvas.height = viewport.height;
    var ctx = canvas.getContext('2d');
    var renderTask = pdfPage.render({
      canvasContext: ctx,
      viewport: viewport,
    });
    return renderTask.promise;
  });
}).catch(function (reason) {
  console.error('Error: ' + reason);
});
