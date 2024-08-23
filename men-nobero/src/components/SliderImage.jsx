function SliderImage({ image, index }) {
  return (
    <div className={"carousel-item" + (index == 0 ? " active" : "")}>
      <img src={image} className="image-fluid d-block w-100" alt="..." />
    </div>
  );
}

export default SliderImage;
