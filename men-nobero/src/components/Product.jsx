import Description from "./Description";
import Slider from "./Slider";
import Details from "./Details";
import Features from "./Features";
import api from "../api";
import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

function Product() {
  let [product, setProduct] = useState({});

  let { id } = useParams();

  useEffect(() => {
    getProduct();
  }, [id]);

  const getProduct = () => {
    api
      .get(`/products/${id}`)
      .then((res) => res.data)
      .then((data) => setProduct({ ...data[0] }))
      .catch((err) => {
        alert(err);
        console.log(err);
      });
  };

  return (
    <main className="d-flex m-5 flex-column">
      <div className="d-flex">
        <div className="left col-4 m-md-3">
          {product.id ? <Slider id={product.id} /> : null}
        </div>
        <div className="col-8">
          {product ? <Details product={product} /> : null}
        </div>
      </div>
      <div className="d-flex flex-column">
        <div>{product ? <Features product={product} /> : null}</div>
        <div>
          {product.description ? (
            <Description description={product.description} />
          ) : null}
        </div>
      </div>
    </main>
  );
}

export default Product;
