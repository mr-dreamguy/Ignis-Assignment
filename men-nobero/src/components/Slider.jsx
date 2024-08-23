import SliderButton from "./SliderButton";
import SliderImage from "./SliderImage";
import SliderSlideButtons from "./SliderSlideButtons";
import api from "../api";
import { useState, useEffect } from "react";

function Slider({ id }) {
  let [images, setImages] = useState([]);

  useEffect(() => {
    getImages();
  }, [id]);

  let getImages = () => {
    api
      .get(`images/${id}`)
      .then((res) => res.data)
      .then((data) => setImages(data))
      .catch((err) => {
        alert(err);
        console.log(err);
      });
  };

  return (
    <>
      <div id="carouselExampleIndicators" className="carousel slide">
        <div className="carousel-indicators">
          {images.map((item, idx) => (
            <SliderButton key={idx} index={idx} />
          ))}
        </div>
        <div
          className="carousel-inner"
          style={{ maxHeight: "480px", minHeight: "100px" }}
        >
          {images.map((image, idx) => (
            <SliderImage key={idx} index={idx} image={image.url} />
          ))}
        </div>
        <SliderSlideButtons />
      </div>
    </>
  );
}

export default Slider;
