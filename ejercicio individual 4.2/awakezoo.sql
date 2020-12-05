--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 13.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: animales; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.animales (
    id bigint NOT NULL,
    animal character varying(25),
    nombre character varying(25),
    origen character varying(25),
    nacimiento numeric
);


ALTER TABLE public.animales OWNER TO postgres;

--
-- Name: animales_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.animales_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.animales_id_seq OWNER TO postgres;

--
-- Name: animales_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.animales_id_seq OWNED BY public.animales.id;


--
-- Name: clima; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clima (
    id bigint NOT NULL,
    zona character varying(25),
    humedad numeric,
    t_promedio numeric,
    flora character varying(25)
);


ALTER TABLE public.clima OWNER TO postgres;

--
-- Name: clima_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.clima_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.clima_id_seq OWNER TO postgres;

--
-- Name: clima_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.clima_id_seq OWNED BY public.clima.id;


--
-- Name: detalle; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.detalle (
    id bigint NOT NULL,
    clase character varying(25),
    "alimentaci¢n" character varying(25),
    "reproducci¢n" character varying(25),
    "respiraci¢n" character varying(25),
    sangre character varying(25)
);


ALTER TABLE public.detalle OWNER TO postgres;

--
-- Name: detalle_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.detalle_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.detalle_id_seq OWNER TO postgres;

--
-- Name: detalle_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.detalle_id_seq OWNED BY public.detalle.id;


--
-- Name: tipo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tipo (
    id bigint NOT NULL,
    tipo character varying(25),
    cantidad numeric,
    sector character varying(25),
    responsable character varying(25)
);


ALTER TABLE public.tipo OWNER TO postgres;

--
-- Name: tipo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tipo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tipo_id_seq OWNER TO postgres;

--
-- Name: tipo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tipo_id_seq OWNED BY public.tipo.id;


--
-- Name: animales id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.animales ALTER COLUMN id SET DEFAULT nextval('public.animales_id_seq'::regclass);


--
-- Name: clima id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clima ALTER COLUMN id SET DEFAULT nextval('public.clima_id_seq'::regclass);


--
-- Name: detalle id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle ALTER COLUMN id SET DEFAULT nextval('public.detalle_id_seq'::regclass);


--
-- Name: tipo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo ALTER COLUMN id SET DEFAULT nextval('public.tipo_id_seq'::regclass);


--
-- Data for Name: animales; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.animales (id, animal, nombre, origen, nacimiento) FROM stdin;
1	oso polar	Nevi	Alaska	1990
2	leon	Lionel	T£nez	2001
3	nutria	Ronald	Brasil	2008
4	pez globo	GLovix	Brasil	2012
5	mantaraya	Manti	Cuba	2008
6	tigre	Tony	China	2013
7	elefante	Elias	T£nez	1975
8	cocodrilo	Cody	Egipto	1986
9	avestruz	Aby	Sudafrica	2006
\.


--
-- Data for Name: clima; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.clima (id, zona, humedad, t_promedio, flora) FROM stdin;
1	tropical	90	24	abundante
2	seco	30	20	escasa
3	templado	50	14	media
4	continental	60	10	abundante
5	polar	40	-60	inexistente
\.


--
-- Data for Name: detalle; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.detalle (id, clase, "alimentaci¢n", "reproducci¢n", "respiraci¢n", sangre) FROM stdin;
1	mamiferos	omnivoro	viviparo	pulmones	caliente
2	artropodos	omnivoro	larvas	branquias	fria
3	aves	insectivoro	ov¡paro	pulmones	caliente
4	peces	omnivoro	externa	branquias	fria
5	reptiles	omnivoros	ov¡paro	branquias	fria
6	anfibios	omnivoros	iv¡paro	combinada	fria
7	moluscos	microrganismos	externa	branquias	fria
\.


--
-- Data for Name: tipo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tipo (id, tipo, cantidad, sector, responsable) FROM stdin;
1	mamiferos	14	sabana	Ignacio Idalsoaga
2	artropodos	260	insectario	Alfredo Ugarte
3	aves	80	pajarera	Ignacio Idalsoaga
4	peces	65	acuario	Igancio Idalsoaga
5	resptiles	40	pantano	Sebasti n Jim‚nez
6	anfibios	36	acuario	Sebasti n Jim‚nez
\.


--
-- Name: animales_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.animales_id_seq', 9, true);


--
-- Name: clima_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.clima_id_seq', 5, true);


--
-- Name: detalle_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.detalle_id_seq', 7, true);


--
-- Name: tipo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tipo_id_seq', 6, true);


--
-- PostgreSQL database dump complete
--

