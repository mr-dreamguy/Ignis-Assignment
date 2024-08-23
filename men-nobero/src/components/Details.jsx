import Variants from "./Variants";
import "../styles/Details.css";

function Details({ product }) {
  return (
    <>
      <h1 className="mb-3">{product.title}</h1>
      <div className="d-flex flex-column gap-2 mb-3">
        <span className="price">
          {product.price}&nbsp;
          {/* <span className="discount">{product.mrp + " " + product.price}</span> */}
        </span>
        <span className="mrp">
          MRP:&nbsp;
          <span style={{ textDecoration: "line-through" }}>{product.mrp}</span>
          &nbsp;Inclusive of all Taxes
        </span>
        <span className="weekly-sale">
          {product.weekly_sale} people bought in last 7 days
        </span>
      </div>
      {product.id ? <Variants className="mb-3" id={product.id} /> : null}
    </>
  );
}

export default Details;
