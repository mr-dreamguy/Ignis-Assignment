import Slider from "./Slider";
import "../styles/Details.css";

function ImageCard({ product }) {
  return (
    <div>
      <div className="card" style={{ width: "18rem" }}>
        {/* <img src={product.images} className="card-img-top" alt="..." /> */}
        <Slider id={product.id} />
        <div className="card-body">
          <p className="card-text">
            {product.title} <br />
            <span className="price">{product.price}</span> &nbsp;
            <span className="mrp" style={{ textDecoration: "line-through" }}>
              {product.mrp}
            </span>
            {/* <span className="discount">
              {product.mrp + " " + product.price}
            </span> */}
          </p>
        </div>
      </div>
    </div>
  );
}

export default ImageCard;
