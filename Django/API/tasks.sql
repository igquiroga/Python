-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-10-2023 a las 22:46:51
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tasks`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_tasks`
--

CREATE TABLE `api_tasks` (
  `task_id` int(11) NOT NULL,
  `task_title` varchar(255) NOT NULL,
  `task_date` date NOT NULL,
  `task_description` longtext NOT NULL,
  `task_status` tinyint(1) NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `api_tasks`
--

INSERT INTO `api_tasks` (`task_id`, `task_title`, `task_date`, `task_description`, `task_status`, `user_id`) VALUES
(1, 'Revisar api', '2023-07-31', 'Revisar la api creada que funcione bien', 0, 1),
(2, 'Revisar css', '2023-08-04', 'Revisar el css de las cosas', 1, 1),
(3, 'Probando Api', '2023-08-04', 'Probando mi api', 0, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `authtoken_token`
--

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`) VALUES
('74fc2521e898b74be4e0732164b84490f8f196b4', '2023-07-31 18:51:13.495731', 1),
('a7c5b085782606b9c446ab993ec3f4997c99f87a', '2023-08-04 20:11:22.800295', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add tasks', 7, 'add_tasks'),
(26, 'Can change tasks', 7, 'change_tasks'),
(27, 'Can delete tasks', 7, 'delete_tasks'),
(28, 'Can view tasks', 7, 'view_tasks'),
(29, 'Can add tasks user', 8, 'add_tasksuser'),
(30, 'Can change tasks user', 8, 'change_tasksuser'),
(31, 'Can delete tasks user', 8, 'delete_tasksuser'),
(32, 'Can view tasks user', 8, 'view_tasksuser'),
(33, 'Can add Token', 9, 'add_token'),
(34, 'Can change Token', 9, 'change_token'),
(35, 'Can delete Token', 9, 'delete_token'),
(36, 'Can view Token', 9, 'view_token'),
(37, 'Can add token', 10, 'add_tokenproxy'),
(38, 'Can change token', 10, 'change_tokenproxy'),
(39, 'Can delete token', 10, 'delete_tokenproxy'),
(40, 'Can view token', 10, 'view_tokenproxy');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$390000$EWLeQElMNpKhiRptpNmTrS$E07UqeYrQODDhGcjmWKrhjo7+5sGTCHUOuKMuAb17WU=', '2023-08-04 20:08:04.367661', 0, 'admin', '', '', '', 0, 1, '2023-07-31 18:51:06.134225'),
(2, 'pbkdf2_sha256$390000$I9jeju5nn6BfvhDyV0MVPj$0yyr6opLPZwa+GIWdlUVt8NJCfO3skGzY2kCpBXM7oY=', '2023-08-04 20:11:18.275872', 0, 'nachito', '', '', '', 0, 1, '2023-08-04 20:11:18.082255');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'api', 'tasks'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(9, 'authtoken', 'token'),
(10, 'authtoken', 'tokenproxy'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(8, 'webapi', 'tasksuser');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-07-31 18:49:51.846931'),
(2, 'auth', '0001_initial', '2023-07-31 18:49:52.378162'),
(3, 'admin', '0001_initial', '2023-07-31 18:49:52.508697'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-07-31 18:49:52.517211'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-07-31 18:49:52.525888'),
(6, 'api', '0001_initial', '2023-07-31 18:49:52.542740'),
(7, 'api', '0002_rename_taks_id_tasks_task_id', '2023-07-31 18:49:52.559786'),
(8, 'api', '0003_alter_tasks_task_status', '2023-07-31 18:49:52.564080'),
(9, 'api', '0004_tasks_user_id', '2023-07-31 18:49:52.580402'),
(10, 'contenttypes', '0002_remove_content_type_name', '2023-07-31 18:49:52.661708'),
(11, 'auth', '0002_alter_permission_name_max_length', '2023-07-31 18:49:52.718062'),
(12, 'auth', '0003_alter_user_email_max_length', '2023-07-31 18:49:52.740112'),
(13, 'auth', '0004_alter_user_username_opts', '2023-07-31 18:49:52.747875'),
(14, 'auth', '0005_alter_user_last_login_null', '2023-07-31 18:49:52.874716'),
(15, 'auth', '0006_require_contenttypes_0002', '2023-07-31 18:49:52.878715'),
(16, 'auth', '0007_alter_validators_add_error_messages', '2023-07-31 18:49:52.885744'),
(17, 'auth', '0008_alter_user_username_max_length', '2023-07-31 18:49:52.909511'),
(18, 'auth', '0009_alter_user_last_name_max_length', '2023-07-31 18:49:52.929892'),
(19, 'auth', '0010_alter_group_name_max_length', '2023-07-31 18:49:52.952436'),
(20, 'auth', '0011_update_proxy_permissions', '2023-07-31 18:49:52.962143'),
(21, 'auth', '0012_alter_user_first_name_max_length', '2023-07-31 18:49:52.982179'),
(22, 'authtoken', '0001_initial', '2023-07-31 18:49:53.068941'),
(23, 'authtoken', '0002_auto_20160226_1747', '2023-07-31 18:49:53.093203'),
(24, 'authtoken', '0003_tokenproxy', '2023-07-31 18:49:53.098520'),
(25, 'sessions', '0001_initial', '2023-07-31 18:49:53.131624'),
(26, 'webapi', '0001_initial', '2023-07-31 18:49:53.163748'),
(27, 'webapi', '0002_tasksuser_delete_usuariostareas', '2023-07-31 18:49:53.186385');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('8ubx6zs0bjj0hdog9c7wywl9xzxs1q38', '.eJxVjDsOwjAQBe_iGlne-JNdSnrOYHn9wQHkSHFSIe4OkVJA-2bmvYQP21r91vPipyTOAsTpd-MQH7ntIN1Du80yzm1dJpa7Ig_a5XVO-Xk53L-DGnr91pSQHUVEQ5gAHZdQCEeNJqsceIAUC1kiVUBpO8CgC4MiB5ZGNJrF-wPZhzcH:1qQXz0:p9JHjdYCNWX67B9iCf2y93D9gNf0AOVNpcUMzbHZ3Fw', '2023-08-14 18:51:06.328624'),
('jcwlkh26uc4zx26jgaavn51380yzpsa4', '.eJxVjDsOwjAQBe_iGlne-JNdSnrOYHn9wQHkSHFSIe4OkVJA-2bmvYQP21r91vPipyTOAsTpd-MQH7ntIN1Du80yzm1dJpa7Ig_a5XVO-Xk53L-DGnr91pSQHUVEQ5gAHZdQCEeNJqsceIAUC1kiVUBpO8CgC4MiB5ZGNJrF-wPZhzcH:1qQcrw:bUr6GBk8uv5PXsLK5_meZP0VRjFStEH4hl9mr6l84iU', '2023-08-15 00:04:08.813014'),
('v1h5pgji772lvi6drpgk4cykuv7f70ti', '.eJxVjEsOwjAMBe-SNYoa18QpS_Y9Q-XYFi2gROpnhbg7VOoCtm9m3ssNvK3jsC02D5O6iwN3-t0yy8PKDvTO5Va91LLOU_a74g-6-L6qPa-H-3cw8jJ-60hBY5sABDvO0nWUlaQVSlExhJCUkwBFQEKDBhOGrA1Zi2aB4ezeH8hPNxY:1qS18o:I8GOKl_Rpn9YzwtiXCPntg7VVpj0t0aEO9liDT16XD8', '2023-08-18 20:11:18.278943');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `webapi_tasksuser`
--

CREATE TABLE `webapi_tasksuser` (
  `user_id` int(11) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `user_password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `api_tasks`
--
ALTER TABLE `api_tasks`
  ADD PRIMARY KEY (`task_id`);

--
-- Indices de la tabla `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `webapi_tasksuser`
--
ALTER TABLE `webapi_tasksuser`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `api_tasks`
--
ALTER TABLE `api_tasks`
  MODIFY `task_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `webapi_tasksuser`
--
ALTER TABLE `webapi_tasksuser`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
