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
    </div>
  );
};
export default Reviews;
