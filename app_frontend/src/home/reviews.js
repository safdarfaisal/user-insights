import Review from '../reusable/Reviews.js';
import { useState, useEffect } from 'react'
import './reviews.css';
import React from 'react';


const Reviews = () => {
  const [reviews, setReviews] = useState([]);
  
  useEffect(() => {
    getReviewList();
  }, []);

  const getReviewList = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/movies/reviews/', {
        method: 'GET',
        headers: {
          'Content-Type' : 'application/json',
          'Accept' : 'application/json',
        },
      });
      const data = await response.json();
      
      if(response.status === 200){
        setReviews(data);
      }
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className='reviewsBoxContainer'>
      {reviews.map((review) => {
        return (
          <Review 
          movieName={review.movie_name} 
          stars={review.rating}
          userName={review.user_name}
          review={review.review} />
        )
      })}
      {/* // <Review movieName='Fast and Furious 1' stars={2.5} />
      // <Review movieName='Fast and Furious 2' stars={5} />
      // <Review movieName='Fast and Furious 3' stars={3.5} />
      // <Review movieName='Fast and Furious 4' stars={4.5} />
      // <Review movieName='Fast and Furious 5' stars={5} /> */}
    </div>
  );
};
export default Reviews;
