from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, List, Union, Dict, Mapping, Any

from .flags import MessageFlags, AttachmentFlags, SystemChannelFlags, RoleFlags, GuildMemberFlags, \
    UserFlags, ChannelFlags
from .sentinels import MISSING, DEPRECATED
from .types import InteractionType, ApplicationCommandType, InteractionContextType, \
    ApplicationIntegrationType, \
    ApplicationCommandOptionType, InteractionCallbackType, EmbedType, ComponentType, ButtonStyle, ChannelType, \
    TextInputStyle, LayoutType, AllowedMentionType, VerificationLevel, DefaultMessageNotificationLevel, MFALevel, \
    PremiumTier, GuildNSFWLevel, PremiumType, MessageReferenceType, MessageActivityType, MessageType, StickerType, \
    StickerFormatType, VideoQualityMode, ForumLayoutType, SortOrderType

"""Describes most of Discord object used in their API as dataclasses"""

class Snowflake(int):
    """Represents Discord Snowflake as an integer"""

    @property
    def timestamp(self):
        return (self >> 22) + 1420070400000

    @property
    def internal_worker_id(self):
        return (self & 0x3E0000) >> 17

    @property
    def internal_process_id(self):
        return (self & 0x1F000) >> 12

    @property
    def increment(self):
        return self & 0xFFF


@dataclass
class AllowedMentions:
    parse: List[AllowedMentionType]
    roles: List[Snowflake]
    users: List[Snowflake]
    replied_user: bool = field(default=False)


@dataclass
class Attachment:
    id: Snowflake
    filename: str
    size: int
    url: str
    proxy_url: str
    title: Optional[str] = field(default=MISSING)
    description: Optional[str] = field(default=MISSING)
    content_type: Optional[str] = field(default=MISSING)
    height: Optional[str] = field(default=MISSING)
    width: Optional[str] = field(default=MISSING)
    ephemeral: Optional[bool] = field(default=MISSING)
    duraction_secs: Optional[float] = field(default=MISSING)
    waveform: Optional[str] = field(default=MISSING)
    flags: Optional[AttachmentFlags] = field(default=MISSING)


@dataclass
class ApplicationCommand:
    id: Snowflake
    application_id: Snowflake
    name: str
    description: str
    version: Snowflake
    type: Optional[ApplicationCommandType] = field(default=ApplicationCommandType.CHAT_INPUT)
    guild_id: Optional[Snowflake] = field(default=MISSING)
    name_localizations: Optional[Dict[str]] = field(default=MISSING)
    description_localizations: Optional[Dict[str]] = field(default=MISSING)
    options: Optional[List[ApplicationCommandOption]] = field(default=MISSING)
    default_member_permissions: Optional[str] = field(default=MISSING)
    dm_permission: Optional[bool] = field(default=DEPRECATED)
    default_permission: Optional[bool] = field(default=DEPRECATED)
    nsfw: Optional[bool] = field(default=MISSING)
    integration_types: Optional[List[ApplicationIntegrationType]] = field(default=MISSING)
    contexts: Optional[List[InteractionContextType]] = field(default=MISSING)


@dataclass
class ApplicationCommandInteractionOption:
    name: str
    type: ApplicationCommandOptionType
    value: Optional[Union[str, int, float, bool]] = field(default=MISSING)
    options: Optional[List[ApplicationCommandInteractionOption]] = field(default=MISSING)
    focused: Optional[bool] = field(default=MISSING)


@dataclass
class ApplicationCommandOption:
    type: ApplicationCommandOptionType
    name: str
    description: str
    name_localizations: Optional[Dict[str]] = field(default=MISSING)
    description_localizations: Optional[Dict[str]] = field(default=MISSING)
    required: Optional[bool] = field(default=False)
    choices: Optional[List[ApplicationCommandOption]] = field(default=MISSING)
    options: Optional[List[ApplicationCommandOption]] = field(default=MISSING)
    channel_types: Optional[List[ChannelType]] = field(default=MISSING)
    min_value: Optional[Union[int, float]] = field(default=MISSING)
    max_value: Optional[Union[int, float]] = field(default=MISSING)
    autocomplete: Optional[bool] = field(default=MISSING)


@dataclass
class Interaction:
    id: Snowflake
    application_id: Snowflake
    version: int
    token: str
    type: InteractionType
    entitlements: List[Entitlement]
    authorizing_integration_owners: AuthorizingIntegrationOwners
    data: Optional[InteractionData] = field(default=MISSING)
    guild: Optional[Guild] = field(default=MISSING)
    guild_id: Optional[Snowflake] = field(default=MISSING)
    channel: Optional[Channel] = field(default=MISSING)
    channel_id: Optional[Snowflake] = field(default=MISSING)
    member: Optional[Member] = field(default=MISSING)
    user: Optional[User] = field(default=MISSING)
    message: Optional[Message] = field(default=MISSING)
    app_permissions: Optional[str] = field(default=MISSING)
    locale: Optional[str] = field(default=MISSING)
    guild_locale: Optional[str] = field(default=MISSING)
    context: Optional[InteractionContextType] = field(default=MISSING)


class InteractionCallbackData:
    @dataclass
    class Message:
        tts: Optional[bool] = field(default=MISSING)
        context: Optional[str] = field(default=MISSING)
        embeds: Optional[List[Embed]] = field(default=MISSING)
        allowed_mentions: Optional[AllowedMentions] = field(default=MISSING)
        flags: Optional[MessageFlags] = field(default=MISSING)
        components: Optional[List[Component]] = field(default=MISSING)
        attachments: Optional[List[Attachment]] = field(default=MISSING)
        poll: Optional[Poll] = field(default=MISSING)

    @dataclass
    class Autocomplete:
        choice: List[Choices]

    @dataclass
    class Modal:
        custom_id: str
        title: str
        components: List[Component]


@dataclass
class InteractionData:
    id: Snowflake
    name: str
    type: ApplicationCommandType
    resolved: Optional[ResolvedData] = field(default=MISSING)
    options: Optional[List[ApplicationCommandInteractionOption]] = field(default=MISSING)
    guild_id: Optional[Snowflake] = field(default=MISSING)
    target_id: Optional[Snowflake] = field(default=MISSING)


@dataclass
class InteractionResponse:
    type: InteractionCallbackType
    data: Optional[InteractionCallbackData] = field(default=MISSING)


class Component:
    @dataclass
    class ActionRow:
        type: ComponentType = field(init=False, default=ComponentType.ACTION_ROW)
        components: Optional[List[Component]] = field(default_factory=list)

    @dataclass
    class Buttons:
        style: ButtonStyle
        type: ComponentType = field(init=False, default=ComponentType.BUTTON)
        label: Optional[str] = field(default=MISSING)
        emoji: Optional[Emoji] = field(default=MISSING)
        custom_id: Optional[str] = field(default=MISSING)
        sku_id: Optional[Snowflake] = field(default=MISSING)
        url: Optional[str] = field(default=MISSING)
        disabled: Optional[bool] = field(default=False)

    @dataclass
    class SelectMenu:
        type: ComponentType
        custom_id: str
        options: Optional[List[SelectOption]] = field(default=MISSING)
        channel_types: Optional[List[ChannelType]] = field(default=MISSING)
        placeholder: Optional[str] = field(default=MISSING)
        default_values: Optional[List[SelectDefaultValue]] = field(default=MISSING)
        min_value: Optional[int] = field(default=1)
        max_value: Optional[int] = field(default=1)
        disabled: Optional[bool] = field(default=False)

        @dataclass
        class SelectDefaultValue:
            id: Snowflake
            type: str

        @dataclass
        class SelectOption:
            label: str
            value: str
            description: Optional[str] = field(default=MISSING)
            emoji: Optional[Emoji] = field(default=MISSING)
            default: Optional[bool] = field(default=MISSING)

        def __post_init__(self):
            if self.type not in (ComponentType.TEXT_INPUT, ComponentType.USER_SELECT, ComponentType.ROLE_SELECT,
                                 ComponentType.MENTIONABLE_SELECT, ComponentType.CHANNEL_SELECT):
                raise TypeError(f'Type for {self.__class__.__name__} must be either 3, 5, 6, 7 or 8')

    @dataclass
    class TextInputs:
        type: ComponentType = field(init=False, default=ComponentType.TEXT_INPUT)
        custom_id: str
        style: TextInputStyle
        label: str
        min_length: Optional[int] = field(default=MISSING)
        max_length: Optional[int] = field(default=MISSING)
        required: Optional[bool] = field(default=True)
        value: Optional[str] = field(default=MISSING)
        placeholder: Optional[str] = field(default=MISSING)


@dataclass
class Embed:
    title: Optional[str] = field(default=MISSING)
    type: Optional[EmbedType] = field(default=EmbedType.rich)
    description: Optional[str] = field(default=MISSING)
    url: Optional[str] = field(default=MISSING)
    timestamp: Optional[str] = field(default=MISSING)
    color: Optional[int] = field(default=MISSING)
    footer: Optional[Footer] = field(default=MISSING)
    image: Optional[Image] = field(default=MISSING)
    thumbnail: Optional[Thumbnail] = field(default=MISSING)
    video: Optional[Video] = field(default=MISSING)
    provider: Optional[Provider] = field(default=MISSING)
    author: Optional[Author] = field(default=MISSING)
    fields: Optional[List[Field]] = field(default=MISSING)

    @dataclass
    class Footer:
        text: str
        icon_url: Optional[str] = field(default=MISSING)
        proxy_icon_url: Optional[str] = field(default=MISSING)

    @dataclass
    class Image:
        url: str
        proxy_url: Optional[str] = field(default=MISSING)
        height: Optional[int] = field(default=MISSING)
        width: Optional[int] = field(default=MISSING)

    @dataclass
    class Thumbnail:
        url: str
        proxy_url: Optional[str] = field(default=MISSING)
        height: Optional[int] = field(default=MISSING)
        width: Optional[int] = field(default=MISSING)

    @dataclass
    class Video:
        url: str
        proxy_url: Optional[str] = field(default=MISSING)
        height: Optional[int] = field(default=MISSING)
        width: Optional[int] = field(default=MISSING)

    @dataclass
    class Provider:
        name: Optional[str] = field(default=MISSING)
        url: Optional[str] = field(default=MISSING)

    @dataclass
    class Author:
        name: str
        url: Optional[str] = field(default=MISSING)
        icon_url: Optional[str] = field(default=MISSING)
        proxy_icon_url: Optional[str] = field(default=MISSING)

    @dataclass
    class Field:
        name: str
        value: str
        inline: Optional[bool] = field(default=MISSING)


@dataclass
class Emoji:
    id: Snowflake
    name: str
    roles: Optional[List[Role]] = field(default=MISSING)
    user: Optional[User] = field(default=MISSING)
    require_colons: Optional[bool] = field(default=MISSING)
    managed: Optional[bool] = field(default=MISSING)
    animated: Optional[bool] = field(default=MISSING)
    avalable: Optional[bool] = field(default=MISSING)

    @property
    def partial(self):
        return Emoji(id=self.id, name=self.name, animated=self.animated)


@dataclass
class Poll:
    question: MediaObject
    answers: List[AnswerObject]
    allow_multiselect: bool
    layout_type: LayoutType
    results: Optional[ResultsObject] = field(default=MISSING)
    expiry: Optional[str] = field(default=MISSING)

    @dataclass
    class CreateRequestObject:
        question: Poll.MediaObject
        answers: List[Poll.AnswerObject]
        duration: Optional[int] = field(default=24)
        allow_multiselect: Optional[bool] = field(default=False)
        layout_type: Optional[LayoutType] = field(default=LayoutType.DEFAULT)

    @dataclass
    class MediaObject:
        text: Optional[str] = field(default=MISSING)
        emoji: Optional[Emoji] = field(default=MISSING)

    @dataclass
    class AnswerObject:
        poll_media: Poll.MediaObject
        answer_id: Optional[int] = field(default=MISSING)

    @dataclass
    class ResultsObject:
        is_finalized: bool
        answer_counts: List[Poll.AnswerCountObject]

    @dataclass
    class AnswerCountObject:
        id: int
        count: int
        me_voted: bool


@dataclass
class Guild:
    id: Snowflake
    name: str
    afk_timeout: int
    verification_level: VerificationLevel
    default_message_notifications: DefaultMessageNotificationLevel
    roles: List[Role]
    emojis: List[Emoji]
    features: List[GuildFeatures]
    mfa_level: MFALevel
    system_channel_flags: SystemChannelFlags
    premium_tier: PremiumTier
    nsfw_level: GuildNSFWLevel
    premium_progress_bar_enabled: bool
    icon: Optional[str] = field(default=MISSING)
    icon_hash: Optional[str] = field(default=MISSING)
    splace: Optional[str] = field(default=MISSING)
    discovery_splash: Optional[str] = field(default=MISSING)
    owner: Optional[bool] = field(default=MISSING)
    owner_id: Optional[Snowflake] = field(default=MISSING)
    permissions: Optional[str] = field(default=MISSING)
    region: Optional[str] = field(default=DEPRECATED)
    afk_channel_id: Optional[Snowflake] = field(default=MISSING)
    widget_enabled: Optional[bool] = field(default=MISSING)
    widget_channel_id: Optional[Snowflake] = field(default=MISSING)
    application_id: Optional[Snowflake] = field(default=MISSING)
    system_channel_id: Optional[Snowflake] = field(default=MISSING)
    rules_channel_id: Optional[Snowflake] = field(default=MISSING)
    max_pressences: Optional[int] = field(default=MISSING)
    max_members: Optional[int] = field(default=MISSING)
    vanity_url_code: Optional[str] = field(default=MISSING)
    description: Optional[str] = field(default=MISSING)
    banner: Optional[str] = field(default=MISSING)
    premium_subscription_count: Optional[int] = field(default=MISSING)
    preferred_locale: Optional[str] = field(default=MISSING)
    public_updates_channel_id: Optional[Snowflake] = field(default=MISSING)
    max_video_channel_users: Optional[int] = field(default=MISSING)
    max_stage_video_channel_users: Optional[int] = field(default=MISSING)
    approximate_member_count: Optional[int] = field(default=MISSING)
    approximate_presence_count: Optional[int] = field(default=MISSING)
    welcome_screen: Optional[WelcomeScreen] = field(default=MISSING)
    stickers: Optional[List[Sticker]] = field(default=MISSING)
    safety_alerts_channel_id: Optional[Snowflake] = field(default=MISSING)


@dataclass
class WelcomeScreen:
    welcome_channels: List[WelcomeScreenChannel]
    description: Optional[str] = field(default=MISSING)


@dataclass
class WelcomeScreenChannel:
    channel_id: Snowflake
    description: str
    emoji_id: Optional[Snowflake] = field(default=MISSING)
    emoji_name: Optional[str] = field(default=MISSING)


@dataclass
class Role:
    id: Snowflake
    name: str
    color: int
    hoist: bool
    position: int
    permissions: str
    managed: bool
    mentionable: bool
    flags: RoleFlags
    icon: Optional[str] = field(default=MISSING)
    unicode_emoji: Optional[str] = field(default=MISSING)
    tags: Optional[Tag] = field(default=MISSING)

    @dataclass
    class Tag:
        bot_id: Optional[Snowflake] = field(default=MISSING)
        integration_id: Optional[Snowflake] = field(default=MISSING)
        premium_subscriber: Optional[None] = field(default=MISSING)
        subscription_listing_id: Optional[Snowflake] = field(default=MISSING)
        available_for_purchase: Optional[None] = field(default=MISSING)
        guild_connections: Optional[None] = field(default=MISSING)


@dataclass
class Member:
    roles: List[Snowflake]
    joined_at: str
    deaf: bool
    mute: bool
    flags: GuildMemberFlags
    user: Optional[User] = field(default=MISSING)
    nick: Optional[str] = field(default=MISSING)
    avatar: Optional[str] = field(default=MISSING)
    premium_since: Optional[str] = field(default=MISSING)
    pending: Optional[bool] = field(default=MISSING)
    permissions: Optional[str] = field(default=MISSING)
    communication_disabled_until: Optional[str] = field(default=MISSING)
    avatar_decoration_data: Optional[AvatarDecorationData] = field(default=MISSING)


@dataclass
class User:
    id: Snowflake
    username: str
    discriminator: str
    avatar: Optional[str]
    global_name: Optional[str] = field(default=MISSING)
    bot: Optional[bool] = field(default=MISSING)
    system: Optional[bool] = field(default=MISSING)
    mfa_enabled: Optional[bool] = field(default=MISSING)
    banner: Optional[str] = field(default=MISSING)
    accent_color: Optional[int] = field(default=MISSING)
    locale: Optional[str] = field(default=MISSING)
    verified: Optional[bool] = field(default=MISSING)
    email: Optional[str] = field(default=MISSING)
    flags: Optional[UserFlags] = field(default=MISSING)
    premium_type: Optional[PremiumType] = field(default=MISSING)
    public_flags: Optional[UserFlags] = field(default=MISSING)
    avatar_decoration_data: Optional[AvatarDecorationData] = field(default=MISSING)


@dataclass
class AvatarDecorationData:
    asset: str
    sku_id: Snowflake


@dataclass
class Message:
    id: Snowflake
    channel_id: Snowflake
    author: User
    content: str
    timestamp: str
    tts: bool
    mention_everyone: bool
    mentions: List[User]
    mention_roles: List[Snowflake]
    embeds: List[Embed]
    type: MessageType
    edited_timestamp: Optional[str] = field(default=MISSING)
    mention_channels: Optional[List[ChannelMention]] = field(default=MISSING)
    attachments: Optional[List[Attachment]] = field(default=MISSING)
    reactions: Optional[List[Reaction]] = field(default=MISSING)
    nonce: Optional[Union[int | str]] = field(default=MISSING)
    pinned: Optional[bool] = field(default=MISSING)
    webhook_id: Optional[Snowflake] = field(default=MISSING)
    activity: Optional[Activity] = field(default=MISSING)
    application: Optional[Application] = field(default=MISSING)  # Partial
    application_id: Optional[Snowflake] = field(default=MISSING)
    flags: Optional[MessageFlags] = field(default=MISSING)
    message_reference: Optional[MessageReference] = field(default=MISSING)
    message_snapshots: Optional[List[MessageSnapshot]] = field(default=MISSING)
    referenced_message: Optional[Message] = field(default=MISSING)
    interaction_metadata: Optional[MessageInteractionMetadata] = field(default=MISSING)
    interaction: Optional[MessageInteraction] = field(default=DEPRECATED)
    thread: Optional[Channel] = field(default=MISSING)
    components: Optional[List[Component]] = field(default=MISSING)
    sticker_items: Optional[List[StickerItem]] = field(default=MISSING)
    stickers: Optional[List[Sticker]] = field(default=DEPRECATED)
    position: Optional[int] = field(default=MISSING)
    role_subscription_data: Optional[RoleSubscriptionData] = field(default=MISSING)
    resolved: Optional[ResolvedData] = field(default=MISSING)
    poll: Optional[Poll] = field(default=MISSING)
    call: Optional[MessageCallObject] = field(default=MISSING)


@dataclass
class MessageActivity:
    type: MessageActivityType
    party_id: Optional[Snowflake] = field(default=MISSING)


@dataclass
class MessageReference:
    type: Optional[MessageReferenceType] = field(default=MISSING)
    message_id: Optional[Snowflake] = field(default=MISSING)
    channel_id: Optional[Snowflake] = field(default=MISSING)
    guild_id: Optional[Snowflake] = field(default=MISSING)
    fail_if_not_exists: Optional[bool] = field(default=True)


@dataclass
class MessageSnapshot:
    message: Optional[Message] = field(default=MISSING)


@dataclass
class MessageInteractionMetadata:
    id: Snowflake
    type: InteractionType
    user: Optional[User] = field(default=MISSING)
    authorizing_integration_owners: Dict[ApplicationIntegrationType, Snowflake] = field(
        default=MISSING)  # @todo bien relire la documentation
    original_response_message_id: Optional[Snowflake] = field(default=MISSING)
    interacted_message_id: Optional[Snowflake] = field(default=MISSING)
    triggering_interaction_metadata: Optional[MessageInteractionMetadata] = field(default=MISSING)


@dataclass
class MessageInteraction:
    id: Snowflake
    type: InteractionType
    name: str
    user: User
    member: Optional[Member] = field(default=MISSING)  # partial


@dataclass
class RoleSubscriptionData:
    role_subscription_listing_id: Snowflake
    tier_name: tier_name
    total_months_subscribed: int
    is_renewal: bool


@dataclass
class ResolvedData:
    users: Optional[Mapping[Snowflake, User]] = field(default=MISSING)
    members: Optional[Mapping[Snowflake, Member]] = field(default=MISSING)  # partial
    roles: Optional[Mapping[Snowflake, Role]] = field(default=MISSING)
    channels: Optional[Mapping[Snowflake, Channel]] = field(default=MISSING)  # partial
    messages: Optional[Mapping[Snowflake, Message]] = field(default=MISSING)  # partial
    attachments: Optional[Mapping[Snowflake, Attachment]] = field(default=MISSING)


@dataclass
class MessageCallObject:
    participants: List[Snowflake]
    ended_timestamp: Optional[int] = field(default=MISSING)


@dataclass
class Sticker:
    id: Snowflake
    name: str
    pack_id: Optional[Snowflake] = field(default=MISSING)
    description: Optional[str] = field(default=MISSING)
    tags: Optional[str] = field(default=MISSING)
    asset: Optional[str] = field(default=DEPRECATED)
    type: Optional[StickerType] = field(default=MISSING)
    format_type: Optional[StickerFormatType] = field(default=MISSING)
    available: Optional[bool] = field(default=MISSING)
    guild_id: Optional[Snowflake] = field(default=MISSING)
    user: Optional[User] = field(default=MISSING)
    sort_value: Optional[int] = field(default=MISSING)


@dataclass
class StickerItem:
    id: Snowflake
    name: str
    format_type: StickerFormatType


@dataclass
class StickerPack:
    id: Snowflake
    stickers: List[Sticker]
    name: str
    sku_id: Snowflake
    description: str
    cover_sticker_id: Optional[Snowflake] = field(default=MISSING)
    banner_asset_id: Optional[Snowflake] = field(default=MISSING)


@dataclass
class Channel:
    id: Snowflake
    type: ChannelType
    guild_id: Optional[Snowflake] = field(default=MISSING)
    position: Optional[int] = field(default=MISSING)
    permission_overwrites: Optional[List[PermissionOverwrite]] = field(default=MISSING)
    name: Optional[str] = field(default=MISSING)
    topic: Optional[str] = field(default=MISSING)
    nsfw: Optional[bool] = field(default=MISSING)
    last_message_id: Optional[Snowflake] = field(default=MISSING)
    bitrate: Optional[int] = field(default=MISSING)
    user_limit: Optional[int] = field(default=MISSING)
    rate_limit_per_user: Optional[int] = field(default=MISSING)
    recipients: Optional[List[User]] = field(default=MISSING)
    icon: Optional[str] = field(default=MISSING)
    owner_id: Optional[Snowflake] = field(default=MISSING)
    application_id: Optional[Snowflake] = field(default=MISSING)
    managed: Optional[bool] = field(default=MISSING)
    parent_id: Optional[Snowflake] = field(default=MISSING)
    last_pin_timestamp: Optional[str] = field(default=MISSING)
    rtc_region: Optional[str] = field(default=MISSING)
    video_quality_mode: Optional[VideoQualityMode] = field(default=MISSING)
    message_count: Optional[int] = field(default=MISSING)
    member_count: Optional[int] = field(default=MISSING)
    thread_metadata: Optional[ThreadMetadata] = field(default=MISSING)
    member: Optional[ThreadMember] = field(default=MISSING)
    default_auto_archive_duration: Optional[int] = field(default=MISSING)  # TODO: Create enums for duration
    permissions: Optional[str] = field(default=MISSING)
    flags: Optional[ChannelFlags] = field(default=MISSING)
    total_message_sent: Optional[int] = field(default=MISSING)
    available_tags: Optional[List[ForumTagObject]] = field(default=MISSING)
    applied_tags: Optional[List[Snowflake]] = field(default=MISSING)
    default_reaction_emoji: Optional[DefaultReactionObject] = field(default=MISSING)
    default_thread_rate_limit_per_user: Optional[int] = field(default=MISSING)
    default_sort_order: Optional[SortOrderType] = field(default=MISSING)
    default_forum_layout: Optional[ForumLayoutType] = field(default=MISSING)


@dataclass
class ThreadMember:
    join_timestamp: str
    flags: int  # TODO Create 'Any user-thread settings, currently only used for notifications' ENUM
    id: Optional[Snowflake] = field(default=MISSING)
    user_id: Optional[Snowflake] = field(default=MISSING)
    member: Optional[Member] = field(default=MISSING)


@dataclass
class PermissionOverwrite:
    id: Snowflake
    type: int
    allow: str
    deny: str


@dataclass
class ThreadMetadata:
    archived: bool
    auto_archive_duration: int
    archive_timestamp: str
    locked: bool
    invitable: Optional[bool] = field(default=MISSING)
    create_timestamp: Optional[str] = field(default=MISSING)


@dataclass
class ForumTagObject:
    id: Snowflake
    name: str
    moderated: bool
    emoji_id: Optional[Snowflake] = field(default=MISSING)
    emoji_name: Optional[str] = field(default=MISSING)


@dataclass
class DefaultReactionObject:
    emoji_id: Optional[Snowflake] = field(default=MISSING)
    emoji_name: Optional[str] = field(default=MISSING)


@dataclass
class Reaction:
    count: int
    count_details: ReactionCountDetailsObject
    me: bool
    me_burst: bool
    emoji: Emoji  # partial
    burst_colors: List[Any]  # todo find type for this + find if optional


@dataclass
class ReactionCountDetailsObject:
    burst: int
    normal: int
