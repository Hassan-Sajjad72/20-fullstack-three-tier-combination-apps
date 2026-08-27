import Fastify from "fastify";
import mysql from "mysql2/promise"; async function checkDb(){const c=await mysql.createConnection({host:process.env.DB_HOST,port:Number(process.env.DB_PORT),database:process.env.DB_NAME,user:process.env.DB_USER,password:process.env.DB_PASSWORD,connectTimeout:5000});await c.query("SELECT 1");await c.end();}
const app=Fastify({logger:true});
app.get("/ready", async (_req,reply)=>{try{await checkDb();return {status:"ok",database:"mysql"}}catch{return reply.code(503).send({status:"error"})}});
app.get("/api/v1/message", async()=>({message:"12-react-fastify-mysql is working"}));
await app.listen({host:process.env.HOST||"0.0.0.0",port:Number(process.env.PORT||3000)});
