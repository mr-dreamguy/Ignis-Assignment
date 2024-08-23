import api from "../api";
import { useState, useEffect } from "react";
import ImageCard from "./ImageCard";

function ImageCards({ id }) {
  let [products, setProducts] = useState([]);

  useEffect(() => {
    getProducts();
  }, [id]);

  let getProducts = () => {
    api
      .get(`/category/${id}/products`)
      .then((res) => res.data)
      .then((data) => setProducts(data))
      .catch((err) => {
        alert(err);
        console.log(err);
      });
  };

  return (
    <div className="container text-center ms-auto">
      <div className="row row-cols-1 row-cols-sm-2 row-cols-md-4 ms-auto">
        {products.map((product) => (
          <div className="col m-2" key={product.id}>
            <a
              style={{ textDecoration: "None" }}
              href={`/product/${product.id}`}
            >
              <ImageCard product={product} />
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ImageCards;
