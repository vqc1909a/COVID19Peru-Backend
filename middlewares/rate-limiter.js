const redis = require("../config/redis-client");

const rateLimiter = ({time_restore, number_requests}) => async (req, res, next) => {
  
  const ip = (req.headers["x-forwarded-for"] || req.socket.remoteAddress).slice(0,9);
  const host = req.get("host");
  const isLocal = ip === `${process.env.REDIS_HOST}` || ip === `::ffff:${process.env.REDIS_HOST}` || ip === "::1" || host.indexOf("localhost") !== -1;

  if(!isLocal){
    const requests = await redis.incr(ip);
    let ttl = time_restore;
    if(requests === number_requests + 1){
      await redis.expire(ip, ttl);
    }else{
      ttl = await redis.ttl(ip);
    }
    console.log(ip, requests);

    if(requests >= number_requests + 1){
      return res.status(404).json({
        status: 404, message: "Resource not found"
      })
    }

  }
  next();
}


module.exports = rateLimiter;